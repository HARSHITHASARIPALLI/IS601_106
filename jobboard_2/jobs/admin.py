# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024


from django.contrib import admin

# Register your models here.
from .models import Job, JobApplication

admin.site.register(Job)
admin.site.register(JobApplication)
