from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Укажите вашу электронную почту')
    phone = models.CharField(max_length=35, verbose_name='Телефон', help_text='Укажите ваш номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars', default='users/avatars/default_avatar.jpg',
                               verbose_name='Аватар', **NULLABLE)
    country = models.CharField(verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
