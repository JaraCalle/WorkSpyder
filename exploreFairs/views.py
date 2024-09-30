from django.shortcuts import render, get_object_or_404
from .models import JobFair
from fairManagement.models import Aspirant

def view_fairs(request):
    fairs = JobFair.objects.all()  # Obténer todas las ferias desde la base de datos
    return render(request, 'fairs.html', {'fairs': fairs})

def fair_detail_view(request, id):
    fair = get_object_or_404(JobFair, id=id)
    aspirant = None
    if request.user.is_authenticated:
        aspirant = get_object_or_404(Aspirant, user=request.user)
    return render(request, 'detail-fair.html', {'fair': fair, 'aspirant': aspirant})