# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('job_description', models.TextField()),
                ('contract_type', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('working_language', models.CharField(max_length=255)),
                ('job_category', models.CharField(max_length=255)),
                ('job_link', models.URLField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('company_size', models.CharField(blank=True, max_length=255, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
