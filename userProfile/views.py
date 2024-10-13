from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from fairManagement.models import Aspirant

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def view_profile(request):
    aspirant_user = get_object_or_404(Aspirant, user=request.user)
    return render(request, 'profile.html', {'aspirant': aspirant_user, 'user': request.user})

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def edit_profile(request):
    aspirant_user = get_object_or_404(Aspirant, user=request.user)
    return render(request, 'edit_profile.html', {'aspirant': aspirant_user})