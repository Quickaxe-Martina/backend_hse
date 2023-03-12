from django.db import models


class TaskModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    description = models.CharField(max_length=2000, verbose_name="Описание")
    is_done = models.BooleanField(default=False)
    SIZES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'Hight'),
    )
    priority = models.CharField(max_length=1, verbose_name="Приоритет", choices=SIZES)
