# Generated by Django 5.0.1 on 2024-01-12 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_all_todo_created_at_alter_all_todo_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_todo',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
