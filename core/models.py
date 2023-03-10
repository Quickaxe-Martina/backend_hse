from django.db import models


class TaskModel(models.Model):
    objects = None
    name = models.CharField(max_length=250, verbose_name="Имя")
    description = models.CharField(max_length=2000, verbose_name="Описание")
    is_done = models.BooleanField(default=False, verbose_name="Завершено")

    class Priority(models.IntegerChoices):
        low = 1
        medium = 2
        high = 3

    priority = models.IntegerField(choices=Priority.choices, default=2)



