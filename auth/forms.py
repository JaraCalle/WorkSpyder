#Creado para el login
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Correo electrónico'})
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Contraseña'})
    )
class UserRegisterForm(UserCreationForm):

    usable_password = None
    
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Correo electrónico'})
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Contraseña'})
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Confirma Contraseña'})
    )

    class Meta:
        model = CustomUser  # Cambiar a CustomUser
        fields = ['email', 'password1', 'password2']  # Quitar avatar
        help_texts = {k: "" for k in fields}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email