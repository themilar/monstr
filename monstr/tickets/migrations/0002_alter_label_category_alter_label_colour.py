# Generated by Django 4.1.8 on 2023-04-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="label",
            name="category",
            field=models.CharField(
                choices=[
                    ("type", "Type"),
                    ("status", "Status"),
                    ("priority", "Priority"),
                ],
                max_length=10,
                verbose_name="Category of the label",
            ),
        ),
        migrations.AlterField(
            model_name="label",
            name="colour",
            field=models.CharField(
                choices=[
                    ("r", "Red"),
                    ("gn", "Green"),
                    ("b", "Blue"),
                    ("y", "Yellow"),
                    ("gy", "Grey"),
                    ("p", "Purple"),
                ],
                default="gy",
                max_length=10,
                verbose_name="Associated colour",
            ),
        ),
    ]
