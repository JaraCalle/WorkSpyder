from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from fairManagement.models import Aspirant
from .forms import CustomAuthenticationForm, UserRegisterForm
from .utils import hash_email

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True


@user_passes_test(lambda u: not u.is_authenticated, login_url='view_fairs')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # No guardar aún
            
            email = form.cleaned_data['email']

            # Asigna el avatar automáticamente
            user.avatar = hash_email(email)

            user.save()  # Ahora guarda el usuario
            
            aspirant = Aspirant(
                firsrtName="",
                secondName="", 
                lastName="",
                email=user.email,
                phone="",
                user=user
            )
            aspirant.save()
            
            messages.success(request, f'Usuario {email} creado y aspirante registrado.')
            return redirect('auth:login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)