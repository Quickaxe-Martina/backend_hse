from django.db import models


class TodoModel(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=400)
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=2)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'