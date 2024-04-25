# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_jobapplication_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='maximum_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='minimum_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
