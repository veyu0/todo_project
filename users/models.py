from django.db import models


class User(models.Model):
    username = models.CharField('Имя пользователя', unique=True, max_length=64)
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    email = models.EmailField('Почта', unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
