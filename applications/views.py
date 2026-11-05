from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobApplication
from jobs.models import Job
from companies.models import CompanyProfile
from employees.models import EmployeeProfile
from django.contrib import messages
# Create your views here.
@login_required
def apply_job(request, job_id):
    if request.user.role != 'employee':
        return redirect('login')

    if request.method == 'POST':
        job = get_object_or_404(Job, id=job_id, is_active=True)

        employee = get_object_or_404(
            EmployeeProfile,
            user=request.user
        )

        if JobApplication.objects.filter(
            employee=employee,
            job=job
        ).exists():
            messages.warning(request, "You have already applied for this job!")
            return redirect('job_detail', job_id=job.id)

        JobApplication.objects.create(
            employee=employee,
            job=job
        )

        return redirect('job_detail', job_id=job.id)

    return redirect('job_list')

@login_required
def my_applications(request):
    if request.user.role != 'employee':
        return redirect('login')

    employee = get_object_or_404(EmployeeProfile, user=request.user)

    applications = JobApplication.objects.filter(employee=employee)

    return render(request, 'applications/my_applications.html', {
        'applications': applications
    })

@login_required
def company_applicants(request):
    if request.user.role != 'company':
        return redirect('login')

    company = get_object_or_404(
        CompanyProfile,
        user=request.user
    )

    applications = JobApplication.objects.filter(
        job__company=company
    )

    return render(
        request,
        'applications/company_applicants.html',
        {'applications': applications}
    )

@login_required
def applicant_detail(request, application_id):
    if request.user.role != 'company':
        return redirect('login')

    company = get_object_or_404(
        CompanyProfile,
        user=request.user
    )

    application = get_object_or_404(
        JobApplication,
        id=application_id,
        job__company=company
    )

    employee = application.employee

    return render(
        request,
        'applications/applicant_detail.html',
        {'employee': employee}
    )

@login_required
def update_application_status(request, application_id):
    if request.user.role != 'company':
        return redirect('login')

    company = get_object_or_404(
        CompanyProfile,
        user=request.user
    )

    application = get_object_or_404(
        JobApplication,
        id=application_id,
        job__company=company
    )

    if request.method == 'POST':
        status = request.POST.get('status')
        application.status = status
        application.save()

    return redirect('company_applicants')