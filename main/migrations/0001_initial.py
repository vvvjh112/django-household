# Generated by Django 4.2 on 2023-04-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Table",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("cate1", models.IntegerField(blank=True, null=True)),
                ("caption", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
