# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024

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
