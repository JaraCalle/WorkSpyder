from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import user_passes_test
from fairManagement.models import Aspirant
from .forms import CustomAuthenticationForm, UserRegisterForm
from .utils import hash_email

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True


@user_passes_test(lambda u: not u.is_authenticated, login_url='view_fairs')
def register(request):
    next_url = request.GET.get('next', reverse('view_fairs'))
    fair_id = request.GET.get('fair_id', '')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # No guardar aún
            
            email = form.cleaned_data['email']

            # Asigna el avatar automáticamente
            user.avatar = hash_email(email)

            user.save()  # Ahora guarda el usuario
            
            # Crear el perfil de Aspirant
            aspirant = Aspirant(
                firstName="",
                secondName="", 
                lastName="",
                phone="",
                user=user
            )
            aspirant.save()
            
            # Autenticar y loggear al usuario
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)  # Iniciar sesión automáticamente
                redirect_url = f"{reverse('profile:edit_profile')}?next={next_url}"
                if fair_id:  # Solo agrega fair_id si está presente
                    redirect_url += f"&fair_id={fair_id}"

                return redirect(redirect_url)
    
    if request.method == 'GET':
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)