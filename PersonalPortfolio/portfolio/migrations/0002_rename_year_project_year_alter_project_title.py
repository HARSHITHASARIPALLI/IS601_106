# Generated by Django 4.2.10 on 2024-03-30 00:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="Year",
            new_name="year",
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
