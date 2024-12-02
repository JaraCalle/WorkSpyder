from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import *
from exploreFairs.models import JobFair
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_authenticated, login_url='auth:register')
def register_fair(request):
    # Si no es POST, mostrar el formulario de inscripción o manejar otro caso
    if request.method != "POST":
        return redirect('error_inscripcion', message='Ocurrió un error en la inscripción.')

    aspirant = None

    try:
        aspirant = Aspirant.objects.get(user=request.user)
    except Aspirant.DoesNotExist:
        aspirant = None  # Si no existe un aspirante, simplemente no asigna ningún aspirante ¡OJO DEBERIA HABER UN MESSAGE!

    # Si el aspirante no ha llenado la información del perfil (nombre y apellido) se le envia a llenarla
    if aspirant.is_aspirant_data_empty():
        return HttpResponseRedirect(reverse('profile:edit_profile') + '?next=' + request.path)

    fair_id = request.POST.get('fair_id')
    fair = JobFair.objects.get(id=fair_id)

    # Si el aspirante ya se encuentra inscrito
    if FairRegistration.objects.filter(aspirant=aspirant, fair=fair).exists():
        return redirect('management:error_inscripcion', message='Ya estás inscrito en esta feria.')

    registration = FairRegistration(aspirant=aspirant, fair=fair, registrationDate=timezone.now().date())
    registration.save()
    return redirect('successful_inscription', registration_id=registration.id, fair_title=fair.title)

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:register')
def favorite_fair(request):
    if request.method == "POST":
        aspirant_id = request.POST.get('aspirant_id')
        fair_id = request.POST.get('fair_id')
        aspirant = Aspirant.objects.get(id=aspirant_id)
        fair = JobFair.objects.get(id=fair_id)

        if FairFavorite.objects.filter(aspirant=aspirant, fair=fair).exists():
            FairFavorite.objects.filter(aspirant=aspirant, fair=fair).delete()
        else:
            favorite = FairFavorite(aspirant=aspirant, fair=fair, favoriteDate=timezone.now().date())
            favorite.save()

        return redirect("fair", fair_id)


def error_inscripcion(request, message):
    return render(request, 'error-inscripcion.html', {'message': message})
