# Generated by Django 4.1.8 on 2023-05-02 18:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0006_remove_label_ticket_label_ticket"),
    ]

    operations = [
        migrations.RenameField(
            model_name="label",
            old_name="ticket",
            new_name="tickets",
        ),
    ]
