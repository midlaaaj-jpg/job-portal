from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('company-applicants/', views.company_applicants, name='company_applicants'),
    path('applicant/<int:application_id>/', views.applicant_detail, name='applicant_detail'),
    path('update-status/<int:application_id>/', views.update_application_status, name='update_application_status'),
]