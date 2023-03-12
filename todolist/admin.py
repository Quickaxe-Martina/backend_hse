from django.contrib import admin
from . import models
from .forms import TodoForm


@admin.register(models.TodoModel)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_done', 'priority')
    form = TodoForm