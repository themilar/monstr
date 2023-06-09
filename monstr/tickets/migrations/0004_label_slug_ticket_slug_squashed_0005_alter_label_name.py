# Generated by Django 4.1.8 on 2023-04-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ("tickets", "0004_label_slug_ticket_slug"),
        ("tickets", "0005_alter_label_name"),
    ]

    dependencies = [
        ("tickets", "0003_alter_label_colour"),
    ]

    operations = [
        migrations.AddField(
            model_name="label",
            name="slug",
            field=models.SlugField(default="slug", unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ticket",
            name="slug",
            field=models.SlugField(default="slug", unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="label",
            name="name",
            field=models.CharField(
                help_text="Enter the name of the label",
                max_length=20,
                unique=True,
                verbose_name="Name of the label",
            ),
        ),
    ]
