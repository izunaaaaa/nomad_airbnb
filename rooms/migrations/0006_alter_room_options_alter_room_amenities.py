# Generated by Django 4.1.5 on 2023-01-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0005_alter_room_amenities"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(related_name="rooms", to="rooms.amenity"),
        ),
    ]
