#Creado para el login
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nombre de usuario'})
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Contraseña'})
    )

class UserRegisterForm(UserCreationForm):
    usable_password = None

    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nombre de usuario'})
    )
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
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}