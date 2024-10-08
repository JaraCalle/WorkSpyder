from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from fairManagement.models import Aspirant
from .forms import CustomAuthenticationForm, UserRegisterForm

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True


@user_passes_test(lambda u: not u.is_authenticated, login_url='view_fairs')
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