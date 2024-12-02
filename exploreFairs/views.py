from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import JobFair
from fairManagement.models import Aspirant
from fairManagement.models import FairRegistration
from django.db.models import Q

def view_fairs(request):
    # Obtener los filtros de la solicitud
    location = request.GET.get('location')
    event_date = request.GET.get('event_date')
    organizer = request.GET.get('organizer')
    title = request.GET.get('title')  # Nuevo filtro por título

    # Filtrar las ferias de acuerdo a los parámetros
    fairs = JobFair.objects.all()

    if location:
        fairs = fairs.filter(
            Q(department__icontains=location) | 
            Q(city__icontains=location) | 
            Q(direction__icontains=location)
        )
    if event_date:
        event_date = request.GET.get('event_date')
    if event_date:
        fairs = fairs.filter(
            Q(start_event_date__lte=event_date) & Q(end_event_date__gte=event_date)
        )
    if organizer:
        fairs = fairs.filter(organizer__email__icontains=organizer)
    if title:
        fairs = fairs.filter(title__icontains=title)  # Filtro por título

    return render(request, 'fairs.html', {'fairs': fairs})

def fair_detail_view(request, id):
    fair = get_object_or_404(JobFair, id=id)
    fair_registration = None

    if request.user.is_authenticated:
        aspirant = Aspirant.objects.get(user=request.user)

    try:
        if FairRegistration.objects.filter(aspirant=aspirant, fair=fair).exists():
            fair_registration = FairRegistration.objects.get(aspirant=aspirant, fair=fair)
    except:
        pass
    
    return render(request, 'detail-fair.html', {'fair': fair, 'fair_registration': fair_registration})