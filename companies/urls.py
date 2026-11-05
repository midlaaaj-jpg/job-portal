from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.company_dashboard, name='company_dashboard'),
    path('create-profile/',views.create_company_profile,name='create_company_profile'),
    path('profile/', views.company_profile_view, name='company_profile_view'),
    
]