from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from exploreFairs.models import JobFair
from .forms import FeriaForm

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def post_home_view(request):
    return render(request, "home.html")

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
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

@user_passes_test(lambda u: u.is_authenticated, login_url='auth:login')
def edit_fair_view(request, feria_id=None):
    if feria_id:
        feria = get_object_or_404(JobFair, id=feria_id)
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
    else:
        form = FeriaForm(instance=feria)
    ferias = JobFair.objects.filter(organizer=request.user)

    return render(request, 'editfair.html', {'form': form, 'ferias': ferias, 'selected_feria': feria})