from django import forms
from .models import Ferias

class FeriaForm(forms.ModelForm):
    class Meta:
        model = Ferias
        fields = ['tituloFeria', 'descFeria', 'fechaFeria',
                  'lugarFeria', 'ponenteFeria', 'imagenFeria']
        widgets = {
            'tituloFeria': forms.TextInput(attrs={'class': 'form-control'}),
            'descFeria': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'fechaFeria': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lugarFeria': forms.TextInput(attrs={'class': 'form-control'}),
            'ponenteFeria': forms.TextInput(attrs={'class': 'form-control'}),
            'imagenFeria': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
