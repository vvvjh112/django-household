# Generated by Django 4.2 on 2023-04-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="table",
            old_name="cate1",
            new_name="ca1",
        ),
        migrations.AddField(
            model_name="table",
            name="DATE",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="table",
            name="ca2",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="table",
            name="ca3",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="table",
            name="ca4",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]