from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.forms import EmployeeProfileForm
from.models import EmployeeProfile
# Create your views here.
@login_required
def employee_dashboard(request):
    if request.user.role !='employee':
        return redirect('login')
    return render(request,'employees/dashboard.html')

@login_required
def create_profile(request):

    if request.user.role != 'employee':
        return redirect('login')
    profile = EmployeeProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST,request.FILES,instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('employee_dashboard')

    else:
        form = EmployeeProfileForm(instance=profile)

    return render(request, 'employees/create_profile.html', {'form': form})