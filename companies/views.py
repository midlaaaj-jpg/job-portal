from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CompanyProfileForm
from .models import CompanyProfile
# Create your views here.
@login_required
def company_dashboard(request):
    if request.user.role != 'company':
        return redirect('login')

    return render(request, 'companies/dashboard.html')

@login_required
def create_company_profile(request):

    if request.user.role != 'company':
        return redirect('login')

    profile, created = CompanyProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = CompanyProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('company_dashboard')

    else:
        form = CompanyProfileForm(instance=profile)

    return render(
        request,
        'companies/create_profile.html',
        {'form': form}
    )

@login_required
def company_profile_view(request):

    if request.user.role != 'company':
        return redirect('login')

    profile = CompanyProfile.objects.filter(
        user=request.user
    ).first()

    if not profile:
        return redirect('create_company_profile')

    return render(
        request,
        'companies/company_profile.html',
        {'profile': profile}
    )