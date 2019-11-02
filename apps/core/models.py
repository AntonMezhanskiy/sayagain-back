from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(
        default=True,
        verbose_name='Активный',
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )

    deleted = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата пометки на удаление',
    )


class Profile(BaseModel):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя',
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия',
    )

    role = models.IntegerField(
        default=0,
        verbose_name='Роль',
        help_text='0 - обычный пользователь',
    )

    confirm_id = models.CharField(
        max_length=36,
        verbose_name='ID регистрации',
    )

    confirmed = models.BooleanField(
        default=False,
        verbose_name='Email подтвержден',
    )

    confirm_created_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата подтверждения',
    )

    phone = models.CharField(
        max_length=20,
        default="",
        blank=True,
        verbose_name='Телефон',
    )


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
