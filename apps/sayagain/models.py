from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel


class Word(BaseModel):
    """Модель данных - Слово"""

    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='words',
        verbose_name='Пользователь',
    )

    word = models.CharField(
        max_length=100,
        default='',
        verbose_name='Word',
    )

    translation = models.CharField(
        max_length=100,
        default='',
        verbose_name='Translation',
    )

    description = models.CharField(
        max_length=500,
        default='',
        blank=True,
        verbose_name='Description',
    )

    example = models.CharField(
        max_length=500,
        default='',
        blank=True,
        verbose_name='Example',
    )

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
