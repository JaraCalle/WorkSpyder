from django import forms
from fairManagement.models import Aspirant

class AspirantForm(forms.ModelForm):

    firstName = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Primer nombre'})
    )
    secondName = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Segundo nombre'})
    )
    lastName = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Apellido'})
    )
    phone = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Número de celular', 'type': 'number', 'minlength':"10", 'maxlength':"10"})
    )

    class Meta:
        model = Aspirant
        fields = ['firstName', 'secondName', 'lastName', 'phone']
        help_texts = {k: "" for k in fields}
