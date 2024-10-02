from django.shortcuts import render, redirect, HttpResponse
from .models import *
from exploreFairs.models import JobFair
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def register_fair(request):
    if request.method == "POST":
        aspirant_id = request.POST.get('aspirant_id')
        fair_id = request.POST.get('fair_id')

        aspirant = Aspirant.objects.get(id=aspirant_id)
        fair = JobFair.objects.get(id=fair_id)

        if FairRegistration.objects.filter(aspirant=aspirant, fair=fair).exists():
            return redirect('error_inscripcion', message='Ya estás inscrito en esta feria.')

        registration = FairRegistration(aspirant=aspirant, fair=fair, registrationDate=timezone.now().date())
        registration.save()
        return redirect('successful_inscription', registration_id=registration.id, fair_title=fair.title)
    
    # Si no es POST, mostrar el formulario de inscripción o manejar otro caso
    return redirect('error_inscripcion', message= 'Ocurrió un error en la inscripción.')

def error_inscripcion(request, message):
    return render(request, 'error-inscripcion.html', {'message': message})