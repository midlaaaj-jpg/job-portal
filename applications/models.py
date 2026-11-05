from django.db import models
from employees.models import EmployeeProfile
from jobs.models import Job

# Create your models here.
class JobApplication(models.Model):
    employee=models.ForeignKey(
        EmployeeProfile,
        on_delete=models.CASCADE
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    applied_at=models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[
        ('pending','Pending'),
        ('shortlisted','Shortlisted'),
        ('rejected','Rejected'),
        ('hired','Hired'),
    ],
    default='pending'
)
    def __str__(self):
                    return self.job.title