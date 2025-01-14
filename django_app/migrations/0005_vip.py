# Generated by Django 5.0 on 2024-01-08 15:08

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0004_alter_item_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "priority",
                    models.IntegerField(
                        blank=True,
                        db_index=True,
                        default=5,
                        max_length=300,
                        verbose_name="Приоритет",
                    ),
                ),
                (
                    "expired",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        default=django.utils.timezone.now,
                        max_length=300,
                        verbose_name="дата и время истечения",
                    ),
                ),
                (
                    "article",
                    models.OneToOneField(
                        blank=True,
                        default="",
                        max_length=100,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_app.item",
                        verbose_name="Объявление",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vip объявление",
                "verbose_name_plural": "Vip объявления",
                "ordering": ("priority", "-expired"),
            },
        ),
    ]
