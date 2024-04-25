# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_remove_jobapplication_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='jobs.job'),
            preserve_default=False,
        ),
    ]
