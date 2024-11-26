from django.shortcuts import render,get_object_or_404, redirect
from .models import QR
from django.contrib.auth.decorators import user_passes_test
from fairManagement.models import FairRegistration
from WorkSpyder.settings import SERVER_IP
from urllib.parse import unquote

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def generateQR(request, registration_id, fair_title):
    registration = get_object_or_404(FairRegistration, id=registration_id)

    # Corrigue el error de que al estar viendo el QR recarguen la página y se generen más QR's
    if QR.objects.filter(registration=registration).exists():        
        qr = get_object_or_404(QR, registration=registration)
    else:
        qr = QR(registration=registration)
        qr.save()

    qr_url = f"http://{ SERVER_IP }/attendance/read-attendance/{ qr.id }"
    
    return render(request, 'successful-inscription.html', {'registration_id': registration_id, 'fair_title': unquote(fair_title), 'qr_url': qr_url})

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def readQR(request, qr_id):
    qr = get_object_or_404(QR, id=qr_id)
    registro = qr.registration
    
    inscrito = registro.aspirant
    feria = registro.fair
    organizador = feria.organizer
    
    # Si el usuario logeado no es el creador de la feria no puede marcar la asistencia
    if organizador != request.user:
        return render(request, 'denied-permission.html')

    qr.set_as_read()

    return render(request, 'read-attendance.html', {'feria': feria, 'inscrito': inscrito})
