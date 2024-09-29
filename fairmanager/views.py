from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Ferias
from .forms import FeriaForm

# Create your views here.
def addfair(request):
    if request.method == 'POST':
        form = FeriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a home
    else:
        form = FeriaForm()
    return render(request, 'addfair.html', {'form': form})

def home(request):
    return render(request, "home.html")

def editfair(request, feria_id=None):
    if feria_id:
        # Si se seleccionó una feria, la cargamos desde la base de datos
        feria = get_object_or_404(Ferias, id=feria_id)
    else:
        feria = None
    if request.method == 'POST':
        if 'selected_fair' in request.POST:
            # Si el usuario seleccionó una feria, cargamos sus datos
            feria_id = request.POST.get('selected_fair')
            return redirect('editfair', feria_id=feria_id)
        # Si el formulario fue enviado con nuevos datos para la feria
        form = FeriaForm(request.POST, request.FILES, instance=feria)
        if form.is_valid():
            form.save()
            return redirect('editfair')  # Redirige a la misma página o donde desees
    else:
        # Si es una solicitud GET, mostramos el formulario vacío o con los datos de la feria
        form = FeriaForm(instance=feria)
        # Cargar todas las ferias para mostrar en el selector
    ferias = Ferias.objects.all()

    return render(request, 'editfair.html', {'form': form, 'ferias': ferias, 'selected_feria': feria})