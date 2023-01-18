# Generated by Django 4.1.5 on 2023-01-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0004_room_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(
                related_name="rooms", to="rooms.amenity", verbose_name="amenities"
            ),
        ),
    ]
