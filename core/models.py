from django.db import models


class TaskModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    description = models.CharField(max_length=2000, verbose_name="Описание")
    is_done = models.BooleanField(default=False)
    priority_levels = models.TextChoices('priority_levels', 'L M H')
    priority = models.CharField(max_length=1, blank=True, choices=priority_levels.choices, default='M')
