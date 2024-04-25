# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='contract_type',
            field=models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Freelance', 'Freelance'), ('Internship', 'Internship')], max_length=50),
        ),
    ]
