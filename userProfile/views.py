from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from fairManagement.models import Aspirant
from fairManagement.models import FairRegistration
from .forms import AspirantForm

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def view_profile(request):
    aspirant_user = get_object_or_404(Aspirant, user=request.user)
    fairs_registration = FairRegistration.objects.filter(aspirant = aspirant_user)
    return render(request, 'profile.html', {'aspirant': aspirant_user, 'user': request.user, 'fairs_registration': fairs_registration})


@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def edit_profile(request):
    aspirant_user = get_object_or_404(Aspirant, user=request.user)
    
    next_url = request.GET.get('next', reverse('profile:view_profile'))
    fair_id = request.GET.get('fair_id', '')
    
    if request.method == 'GET':
        form = AspirantForm(instance=aspirant_user)
    elif request.method == 'POST':
        form = AspirantForm(request.POST, instance=aspirant_user)
        if form.is_valid():
            form.save()
            return redirect(next_url, fair_id)

    return render(request, 'edit_profile.html', {'form': form})
