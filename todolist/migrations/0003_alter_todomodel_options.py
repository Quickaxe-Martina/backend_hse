# Generated by Django 4.1.7 on 2023-03-09 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todomodel_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todomodel',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
