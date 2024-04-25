# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024



from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    CONTRACT_TYPE_CHOICES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Freelance', 'Freelance'),
        ('Internship', 'Internship'),
    ]
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)  
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    working_language = models.CharField(max_length=255)
    job_category = models.CharField(max_length=255)
    job_link = models.URLField(max_length=200)
    contact_email = models.EmailField()
    company_size = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    minimum_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maximum_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return self.job_title


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('screening', 'Screening'),
        ('in consideration', 'In Consideration'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/')
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')

    def __str__(self):
        return f"Application from {self.full_name} for {self.job.job_title}"
