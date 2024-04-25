# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_title',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
    ]
