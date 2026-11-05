from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_job, name='create_job'),
    path('list/',views.job_list, name='job_list'),
    path('detail/<int:job_id>/',views.job_detail,name='job_detail'),
    path('company-jobs/', views.company_jobs, name='company_jobs'),
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('close/<int:job_id>/', views.close_job, name='close_job'),
]