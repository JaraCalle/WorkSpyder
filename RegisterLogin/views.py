from django.shortcuts import render
#agregado para el login
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'usuario {username} creado')
            return redirect('manage')
    else:
        form= UserRegisterForm()

    context = { 'form' : form}
    return render(request, 'RegisterLogin/register.html', context )