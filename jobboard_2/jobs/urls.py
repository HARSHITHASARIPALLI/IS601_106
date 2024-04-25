# Name:Harshitha Saripalli
#UCID :hs759
#Date of Submission: 24-04-2024
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='jobs/login.html', next_page='landing-page'), name='login'),
    path('accounts/login/', LoginView.as_view(template_name='jobs/login.html' , next_page='landing-page'), name='login'),
    path('logout/', LogoutView.as_view(next_page='landing-page'), name='logout'),
    path('find-job/', views.find_job, name='find-job'),
    path('post-job/', views.post_job, name='post-job'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('my-posted-jobs/', views.jobs_posted_dashboard, name='jobs_posted_dashboard'),
    path('jobs/<int:job_id>/applications/', views.view_applications, name='view_applications'),
    path('applications/update-status/<int:application_id>/', views.update_application_status, name='update_application_status'),
]
