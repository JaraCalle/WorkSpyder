from django.shortcuts import render
#agregado para el login
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect
from fairManagement.models import Aspirant
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            aspirant = Aspirant(
                firsrtName="",
                secondName="", 
                lastName="",
                email=user.email,
                phone="",
                user=user
            )
            aspirant.save()
            
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado y aspirante registrado.')
            return redirect('auth:login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)