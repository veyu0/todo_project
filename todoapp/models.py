from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField('Название', max_length=50)
    link = models.CharField('Ссылка на проект', max_length=255)
    users = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Участники')


class ToDo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, verbose_name='Проект')
    text = models.CharField('Текст заметки', max_length=255)
    created = models.DateField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateField(auto_now=True, verbose_name='Обновлен')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    active = models.BooleanField()
