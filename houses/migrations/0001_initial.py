# Generated by Django 4.1.5 on 2023-01-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="House",
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
                ("name", models.CharField(max_length=100)),
                ("price_per_night", models.PositiveIntegerField()),
                ("desciption", models.TextField()),
                ("address", models.CharField(max_length=100)),
                (
                    "is_pet_allow",
                    models.BooleanField(
                        default=True,
                        help_text="반려동물 여부를 확인해주세요",
                        verbose_name="반려동물이 함께하나요?",
                    ),
                ),
            ],
        ),
    ]
