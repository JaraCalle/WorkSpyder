from django import forms
from exploreFairs.models import JobFair 
from .CONST import DEPARTAMENTOS, MUNICIPIOS

class FeriaForm(forms.ModelForm):

    title = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Título del evento'})
    )
    description = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Descripción del evento', 'rows': 4})
    )
    start_event_date = forms.DateField(
        label="",
        widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date', 'placeholder': 'Fecha de inicio'})
    )
    
    end_event_date = forms.DateField(
        label="",
        widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date', 'placeholder': 'Fecha de finalización'})
    )

    department = forms.ChoiceField(
        choices=DEPARTAMENTOS,
        label="",
        widget=forms.Select(attrs={'class': 'form-input', 'id': 'usp-custom-departamento-de-residencia',})
    )

    city = forms.ChoiceField(
        choices=MUNICIPIOS,
        label="",
        widget=forms.Select(attrs={'class': 'form-input', 'id': 'usp-custom-municipio-ciudad'})
    )

    direction = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Dirección'})
    )

    start_hour = forms.TimeField(
        label="",
        widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'time', 'placeholder': 'Hora de inicio'})
    )

    end_hour = forms.TimeField(
        label="",
        widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'time', 'placeholder': 'Hora de cierre'})
    )

    keynote_speaker = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Orador principal'})
    )
    image = forms.URLField(
        label="",
        widget=forms.ClearableFileInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = JobFair
        fields = ['title', 'description', 'start_event_date', 'end_event_date', 'start_hour', 'end_hour', 'department', 'city', 'direction', 'keynote_speaker', 'image']
        help_texts = {k: "" for k in fields}

