from rest_framework import serializers
from . import models


class WordSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(
        source='created',
        format='%Y-%m-%d',
        required=False,
    )

    class Meta:
        model = models.Word
        fields = (
            'id',
            'created_date',
            'word',
            'translation',
            'description',
            'example',
        )
        read_only_fields = (
            'id',
            'created_date',
        )

    def create(self, validated_data):
        request = self.context.get('request')

        instance = models.Word.objects.create(
            user=request.user,
            **validated_data
        )

        return instance
