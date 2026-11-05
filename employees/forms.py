from django import forms
from .models import EmployeeProfile

class EmployeeProfileForm(forms.ModelForm):

    class Meta:
        model = EmployeeProfile
        fields = [
            'full_name',
            'contact',
            'location',
            'skills',
            'education',
            'experience',
            'resume'
        ]

   