from django.db import models
from companies.models import CompanyProfile

# Create your models here.
class Job (models.Model):
    company = models.ForeignKey(
    CompanyProfile,
    on_delete=models.CASCADE
        )
    title = models.CharField()
    description = models.TextField()
    location = models.CharField()
    salary = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
                return self.title
