# Generated by Django 4.1.5 on 2023-01-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0003_room_category_alter_room_amenities_alter_room_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="name",
            field=models.CharField(default="", max_length=100),
        ),
    ]
