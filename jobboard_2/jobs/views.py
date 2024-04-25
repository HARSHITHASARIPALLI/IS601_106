# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomUserCreationForm, JobForm
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication
from .forms import JobApplicationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing-page')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'jobs/signup.html', {'form': form})

def landing_page(request):
    jobs = Job.objects.all()
    contract_types = Job.objects.order_by().values_list('contract_type', flat=True).distinct()
    job_categories = Job.objects.order_by().values_list('job_category', flat=True).distinct()

    # Handle search
    search_query = request.GET.get('search', '')
    if search_query:
        jobs = jobs.filter(job_title__icontains=search_query)

    # Handle filters
    contract_type_query = request.GET.get('contract_type', '')
    if contract_type_query:
        jobs = jobs.filter(contract_type=contract_type_query)

    job_category_query = request.GET.get('job_category', '')
    if job_category_query:
        jobs = jobs.filter(job_category=job_category_query)

    context = {
        'jobs': jobs,
        'contract_types': contract_types,
        'job_categories': job_categories,
        'search_query': search_query,
        'selected_contract_type': contract_type_query,
        'selected_job_category': job_category_query,
    }
    return render(request, 'jobs/landing_page.html', context)

def find_job(request):
    # Your logic here
    return render(request, 'jobs/find_job.html')

@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('landing-page')  # Adjust this to your preferred redirect
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})


@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job  # Set the job here
            application.save()
            return redirect('landing-page')  # Adjust as necessary
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})

@login_required
def user_dashboard(request):
    search_query = request.GET.get('search', '')
    status_query = request.GET.get('status', '')
    
    applications = JobApplication.objects.filter(
        user=request.user, 
        job__job_title__icontains=search_query
    )
    
    if status_query:
        applications = applications.filter(status=status_query)
    
    applications = applications.order_by('-applied_on')
    return render(request, 'jobs/user_dashboard.html', {
        'applications': applications,
        'search_query': search_query,
        'status_query': status_query,
        'status_choices': JobApplication.STATUS_CHOICES,
    })


@login_required
def jobs_posted_dashboard(request):
    # Fetch jobs posted by the current user
    jobs = Job.objects.filter(posted_by=request.user)  
    return render(request, 'jobs/jobs_posted_dashboard.html', {'jobs': jobs})

@login_required
def view_applications(request, job_id):
    job = get_object_or_404(Job, pk=job_id, posted_by=request.user)
    applications = job.applications.all().order_by('-id')
    # Get status choices from the JobApplication model
    status_choices = JobApplication._meta.get_field('status').choices
    return render(request, 'jobs/view_applications.html', {
        'job': job,
        'applications': applications,
        'status_choices': status_choices,
    })

@login_required
def update_application_status(request, application_id):
    if request.method == 'POST':
        application = get_object_or_404(JobApplication, pk=application_id, job__posted_by=request.user)  # Ensures only the job poster can update
        new_status = request.POST.get('status')
        if new_status in dict(application._meta.get_field('status').choices):  # Validates status
            application.status = new_status
            application.save()
            return HttpResponseRedirect(reverse('view_applications', args=[application.job.id]))
    return HttpResponseRedirect(reverse('jobs_posted_dashboard'))
