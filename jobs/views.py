from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from .models import Job
from companies.models import CompanyProfile
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def create_job(request):

    if request.user.role != 'company':
        return redirect('login')

    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.companyprofile
            job.save()

            return redirect('company_dashboard')

    else:
        form = JobForm()

    return render(request, 'jobs/create_job.html', {'form': form})

@login_required
def job_list(request):
    if request.user.role != 'employee':
        return redirect('login')

    jobs = Job.objects.filter(is_active=True)

    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, job_id):
    if request.user.role != 'employee':
        return redirect('login')

    job = get_object_or_404(Job, id=job_id)

    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def company_jobs(request):
    if request.user.role != 'company':
        return redirect('login')

    company = get_object_or_404(CompanyProfile, user=request.user)

    jobs = Job.objects.filter(company=company)

    return render(request, 'jobs/company_jobs.html', {'jobs': jobs})

@login_required
def edit_job(request, job_id):
    if request.user.role != 'company':
        return redirect('login')

    company = get_object_or_404(
        CompanyProfile,
        user=request.user
    )

    job = get_object_or_404(
        Job,
        id=job_id,
        company=company
    )

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            form.save()
            return redirect('company_jobs')

    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/edit_job.html', {'form': form})

@login_required
def close_job(request, job_id):
    if request.user.role != 'company':
        return redirect('login')

    company = get_object_or_404(
        CompanyProfile,
        user=request.user
    )

    job = get_object_or_404(
        Job,
        id=job_id,
        company=company
    )

    if request.method == 'POST':
        job.is_active = False
        job.save()

    return redirect('company_jobs')