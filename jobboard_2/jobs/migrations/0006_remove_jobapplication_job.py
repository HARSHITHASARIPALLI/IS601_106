# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_jobapplication_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='job',
        ),
    ]
