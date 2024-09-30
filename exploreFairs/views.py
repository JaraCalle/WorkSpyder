from django.shortcuts import render, get_object_or_404
from .models import JobFair
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
        fairs = fairs.filter(location__icontains=location)
    if event_date:
        fairs = fairs.filter(event_date=event_date)
    if organizer:
        fairs = fairs.filter(organizer__username__icontains=organizer)
    if title:
        fairs = fairs.filter(title__icontains=title)  # Filtro por título

    return render(request, 'fairs.html', {'fairs': fairs})

def fair_detail_view(request, id):
    fair = get_object_or_404(JobFair, id=id)
    return render(request, 'detail-fair.html', {'fair': fair})