# Generated by Django 4.2.6 on 2024-03-26 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_jobapplication_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('screening', 'Screening'), ('in consideration', 'In Consideration'), ('interview', 'Interview'), ('offer', 'Offer'), ('rejected', 'Rejected')], default='applied', max_length=20),
        ),
    ]
