# Generated by Django 4.1.6 on 2023-02-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="currency",
            field=models.CharField(
                blank=True,
                choices=[("won", "korean Won"), ("usd", "Dollar")],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "Male"), ("female", "Female")],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="language",
            field=models.CharField(
                blank=True,
                choices=[("kr", "Korean"), ("en", "English")],
                max_length=2,
                null=True,
            ),
        ),
    ]
