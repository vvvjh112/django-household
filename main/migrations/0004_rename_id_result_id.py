# Generated by Django 4.2 on 2023-04-26 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_result"),
    ]

    operations = [
        migrations.RenameField(
            model_name="result",
            old_name="ID",
            new_name="id",
        ),
    ]