from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from exploreFairs.models import JobFair
from .forms import FeriaForm

def post_home_view(request):
    return render(request, "home.html")

def add_fair_view(request):
    if request.method == 'POST':
        form = FeriaForm(request.POST, request.FILES)
        if form.is_valid():
            fair = form.save(commit=False)
            fair.organizer = request.user
            fair.save()
            
            return redirect('view_fairs')
    else:
        form = FeriaForm()
    
    return render(request, 'addfair.html', {'form': form})

def edit_fair_view(request, feria_id=None):
    if feria_id:
        feria = get_object_or_404(JobFair, id=feria_id)
    else:
        feria = None
        
    if request.method == 'POST':
        if 'selected_fair' in request.POST:
            feria_id = request.POST.get('selected_fair')
            return redirect('edit_selected_fair', feria_id=feria_id)
        form = FeriaForm(request.POST, request.FILES, instance=feria)
        if form.is_valid():
            form.save()
            return redirect('edit_fair')  
    else:
        form = FeriaForm(instance=feria)
    ferias = JobFair.objects.all()

    return render(request, 'editfair.html', {'form': form, 'ferias': ferias, 'selected_feria': feria})