from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# Собственный класс пользователя (создан только для практики) / Расширение стандартной модели
class User(AbstractUser):
    image = models.ImageField(upload_to='user_profile_images', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
