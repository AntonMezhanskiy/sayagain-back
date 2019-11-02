from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAuthenticated
from . import models, serializers, paginators


class RegisterView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        """Регистрация нового пользователя"""
        serializer = serializers.UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "ok"
            },
            status=status.HTTP_200_OK,
        )


class LoginView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cd = serializer.validated_data
        user = authenticate(request,
                            username=cd['username'].lower(),
                            password=cd['password'])
        if user is not None:
            if not user.profile.confirmed:
                return Response(
                    {
                        "error": 'email_not_confirmed'
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            serializer = serializers.ProfileDetailSerializer(instance=user.profile)
            data = dict()
            data['user'] = serializer.data
            login(request, user)  # Session auth
            return Response(
                data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "error": "wrong_email_or_password"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutView(APIView):
    """Выйти из системы"""

    def post(self, request):
        logout(request)
        return Response(
            {
                'message': 'ok'
            },
            status=status.HTTP_200_OK
        )
