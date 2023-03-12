from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_remove_taskmodel_deadline_remove_taskmodel_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="taskmodel",
            name="priority",
            field=models.CharField(
                choices=[
                    ("high", "Высокий"),
                    ("midium", "Средний"),
                    ("low", "Низкий")
                ],
                default="midium",
                max_length=6,
                verbose_name="Приоритет"
            ),
        ),
    ]
