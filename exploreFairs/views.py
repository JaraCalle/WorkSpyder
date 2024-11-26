from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from .models import JobFair
from .utils import is_aspirant_data_empty
from fairManagement.models import Aspirant
from fairManagement.models import FairRegistration
from django.db.models import Q, F

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

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:register')
def fair_detail_view(request, id):
    fair = get_object_or_404(JobFair, id=id)
    aspirant = None
    if request.user.is_authenticated:
        # Verifica si existe un Aspirant asociado al usuario autenticado
        try:
            aspirant = Aspirant.objects.get(user=request.user)
        except Aspirant.DoesNotExist:
            aspirant = None  # Si no existe, simplemente no asigna ningún aspirante
    
    # Si el aspirante no ha llenado la información del perfil (nombre y apellido) se le envia a llenarla
    if is_aspirant_data_empty(aspirant):
        return HttpResponseRedirect(reverse('profile:edit_profile') + '?next=' + request.path)
    
    if FairRegistration.objects.filter(aspirant=aspirant, fair=fair).exists():
        fair_registration = FairRegistration.objects.get(aspirant=aspirant, fair=fair)
    else:
        fair_registration = None
    
    
    return render(request, 'detail-fair.html', {'fair': fair, 'aspirant': aspirant, 'fair_registration': fair_registration})