from django.db import models
from django.conf import settings

# Create your models here.
class CompanyProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/',null=True,blank=True)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    contact = models.CharField(max_length=12)
    def __str__(self):
            return self.company_name