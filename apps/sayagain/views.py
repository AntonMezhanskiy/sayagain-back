from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import models, serializers, permissions


class WordListView(generics.ListAPIView):
    """Получение списка слов"""
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = serializers.WordSerializer

    def get_queryset(self):
        queryset = models.Word.objects.filter(
            is_active=True,
            user=self.request.user,
        )

        queryset = queryset.order_by('-created')

        return queryset


class WordCreateView(generics.CreateAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = serializers.WordSerializer
    queryset = models.Word.objects.filter(is_active=True)


class WordEditView(generics.UpdateAPIView):
    permission_classes = (
        IsAuthenticated,
        permissions.WordPermission,
    )
    serializer_class = serializers.WordSerializer
    queryset = models.Word.objects.filter(is_active=True)
