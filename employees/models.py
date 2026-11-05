from django.db import models
from django.conf import settings

# Create your models here.
class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    skills = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    resume = models.FileField(
        upload_to='resumes',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.full_name