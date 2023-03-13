from django.db import models


class TaskModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    description = models.CharField(max_length=2000, verbose_name="Описание")
    PRIORITY_CHOICES = [("high", "Высокий"), ("midium",
                                              "Средний"), ("low", "Низкий"),]
    priority = models.CharField(
        max_length=6, choices=PRIORITY_CHOICES, default="midium", verbose_name="Приоритет")
    is_done = models.BooleanField(default=False)
