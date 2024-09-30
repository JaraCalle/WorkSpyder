from django.shortcuts import render,get_object_or_404
from .models import QR
from fairManagement.models import FairRegistration

# Create your views here.
def generateQR(request, registration_id, fair_title):
    registration = get_object_or_404(FairRegistration, id=registration_id)
    qr = QR(registration=registration)
    qr.save()
    return render(request, 'successful-inscription.html', {'registration_id': registration_id, 'fair_title': fair_title,})

def readQR(request):
    return render(request, 'successful-attendance.html')