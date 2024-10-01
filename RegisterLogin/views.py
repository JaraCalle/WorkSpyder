from django.shortcuts import render
#agregado para el login
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'usuario {username} creado')
    else:
        form= UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'register.html', context )