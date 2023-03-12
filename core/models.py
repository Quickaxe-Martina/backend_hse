from django.db import models


class TaskModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    description = models.CharField(max_length=2000, verbose_name="Описание")
    priority = models.CharField(
        default='midium', max_length=6, verbose_name='Приоритет')
    is_done = models.BooleanField(default=False)
