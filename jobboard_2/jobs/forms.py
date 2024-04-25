# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Job
from .models import JobApplication
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)  # Add 'email' if you want the email field

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Here, you can customize each field as needed
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'autocomplete': 'off'})

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company_name', 'logo', 'job_title', 'job_description', 'contract_type',
                  'location', 'working_language', 'job_category', 'job_link', 
                  'contact_email', 'company_size', 'industry', 'minimum_salary', 'maximum_salary']
        widgets = {
            'job_description': forms.Textarea(attrs={'rows': 6}),  # Increased from 3 to 6
            'logo': forms.FileInput(attrs={'accept': 'image/*'}),
        }
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['contract_type'].widget = forms.Select(choices=Job.CONTRACT_TYPE_CHOICES)


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'phone_number', 'cover_letter', 'resume']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 4}),
            'resume': forms.FileInput(attrs={'accept': 'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document'}),
        }


