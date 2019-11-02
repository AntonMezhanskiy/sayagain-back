from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from . import models
from .validators import check_email
from uuid import uuid4


class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(
        required=True,
    )


class ProfileDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        read_only=True,
    )

    class Meta:
        model = models.Profile
        fields = (
            'user_id',
            'first_name',
            'last_name',
            'role',
        )

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.last_name = validated_data.get('last_name',
                                                instance.last_name)

        instance.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = instance.user
        data['email'] = user.username

        return data


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'},
    )
    email = serializers.EmailField(
        required=True,
    )
    first_name = serializers.CharField(
        max_length=100,
        required=True,
    )
    last_name = serializers.CharField(
        max_length=100,
        required=True,
    )

    class Meta:
        model = User
        fields = (
            'password',
            'password2',
            'email',
            'first_name',
            'last_name',
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {
                    "Error": "Пароли не совпадают"
                }
            )
        password2 = data['password2']
        password_validation.validate_password(password2)
        check_email(data['email'])

        return data

    def create(self, validated_data):
        email = validated_data['email'].lower()
        user = User(username=email,
                    email=email)
        user.set_password(validated_data['password'])
        user.save()
        models.Profile.objects.create(
            user=user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            confirmed=True,
            confirm_id=str(uuid4()),
        )

        return user
