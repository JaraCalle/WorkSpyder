from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from exploreFairs.models import JobFair
from fairManagement.models import FairRegistration, FairFavorite, Aspirant
from fairAttendance.models import QR
from .CONST import IMGBB_API_URL
from decouple import config
from .forms import FeriaForm
import requests
import os

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def post_home_view(request):
    return render(request, "home.html")

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def add_fair_view(request):
    if request.method == 'POST':
        form = FeriaForm(request.POST, request.FILES)  # Manejar datos y archivos
        if form.is_valid():
            image_file = request.FILES.get('image')  # Obtener el archivo de la imagen
            
            # Subir el archivo a ImgBB
            try:
                response = requests.post(
                    IMGBB_API_URL,
                    data={'key': config('IMGBB_API_KEY')},
                    files={
                        'image': (image_file.name, image_file.file, image_file.content_type)
                    }
                )
                response_data = response.json()
                
                if response.status_code == 200:
                    # Obtener la URL de la imagen subida
                    img_url = response_data['data']['url']
                    
                    # Guardar la feria en la base de datos
                    fair = form.save(commit=False)  # No guardar todavía
                    fair.organizer = request.user
                    fair.image = img_url  # Asignar la URL
                    fair.save()  # Guardar en la base de datos

                    return redirect('view_fairs')
                else:
                    # Error al subir a ImgBB
                    form.add_error('image', f"Error al subir la imagen: {response_data.get('error', {}).get('message', 'Desconocido')}")
            
            except requests.RequestException as e:
                # Error al realizar la solicitud a ImgBB
                form.add_error('image', f"Error al subir la imagen: {str(e)}")
    else:
        form = FeriaForm()
    
    return render(request, 'addfair.html', {'form': form})

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def edit_fair_view(request, feria_id=None):
    if feria_id:
        feria = get_object_or_404(JobFair, id=feria_id)
        if feria.organizer != request.user:
            return redirect('auth:login')
    else:
        feria = None

    if request.method == 'POST':
        if 'selected_fair' in request.POST:
            feria_id = request.POST.get('selected_fair')
            return redirect('post:edit_selected_fair', feria_id=feria_id)
        form = FeriaForm(request.POST, request.FILES, instance=feria)

        if form.is_valid():
            form.save()
            return redirect('post:edit_fair')
    if feria:
        form = FeriaForm(instance=feria)
    else:
        form = None

    ferias = JobFair.objects.filter(organizer=request.user)
    return render(request, 'editfair.html', {'form': form, 'ferias': ferias, 'selected_feria': feria})

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def view_published_fairs(request):
    ferias = JobFair.objects.filter(organizer=request.user)
    aspirant = get_object_or_404(Aspirant, user=request.user)
    favorites = FairFavorite.objects.filter(aspirant=aspirant)
    fairs_registration = FairRegistration.objects.filter(aspirant = aspirant)
    return render(request, "published_fairs.html", {'ferias': ferias, 'favorites': favorites, 'fairs_registration': fairs_registration})

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def view_registered_fair(request, id):
    fair = get_object_or_404(JobFair, id=id)
    qrs = QR.objects.filter(registration__fair=fair)
    return render(request, 'registered_fair.html', {'fair': fair, 'registers': qrs})

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def delete_selected_fair(request, feria_id):
    feria = get_object_or_404(JobFair, id=feria_id)
    if feria.organizer != request.user:
        return redirect('exploreFairs:view_fairs')
    
    feria.delete()
    return redirect('post:view_published_fairs')