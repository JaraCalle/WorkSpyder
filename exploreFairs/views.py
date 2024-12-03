from django.shortcuts import render, get_object_or_404
from .models import JobFair
from .utils import filter_job_fairs
from fairManagement.models import Aspirant
from fairManagement.models import FairRegistration

def view_fairs(request):
    filters = {
        'location': request.GET.get('location'),
        'event_date': request.GET.get('event_date'),
        'organizer': request.GET.get('organizer'),
        'title': request.GET.get('title'),
    }

    # Aplicar los filtros usando la función auxiliar
    fairs = filter_job_fairs(JobFair.objects.all(), filters)
    
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