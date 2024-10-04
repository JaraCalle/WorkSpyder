from django import forms
from exploreFairs.models import JobFair 

class FeriaForm(forms.ModelForm):
    DEPARTAMENTOS = [
        ('Amazonas', 'Amazonas'),
        ('Antioquía', 'Antioquía'),
        ('Arauca', 'Arauca'),
        ('Atlántico', 'Atlántico'),
        ('Bolívar', 'Bolívar'),
        ('Boyacá', 'Boyacá'),
        ('Caldas', 'Caldas'),
        ('Caquetá', 'Caquetá'),
        ('Casanare', 'Casanare'),
        ('Cauca', 'Cauca'),
        ('Cesar', 'Cesar'),
        ('Chocó', 'Chocó'),
        ('Córdoba', 'Córdoba'),
        ('Cundinamarca', 'Cundinamarca'),
        ('Guainía', 'Guainía'),
        ('Guaviare', 'Guaviare'),
        ('Huila', 'Huila'),
        ('La Guajira', 'La Guajira'),
        ('Magdalena', 'Magdalena'),
        ('Meta', 'Meta'),
        ('Nariño', 'Nariño'),
        ('Norte de Santander', 'Norte de Santander'),
        ('Putumayo', 'Putumayo'),
        ('Quindío', 'Quindío'),
        ('Risaralda', 'Risaralda'),
        ('San Andrés y Providencia', 'San Andrés y Providencia'),
        ('Santander', 'Santander'),
        ('Sucre', 'Sucre'),
        ('Tolima', 'Tolima'),
        ('Valle del Cauca', 'Valle del Cauca'),
        ('Vaupés', 'Vaupés'),
        ('Vichada', 'Vichada'),
    ]

    title = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Título del evento'})
    )
    description = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Descripción del evento', 'rows': 4})
    )
    event_date = forms.DateField(
        label="",
        widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date', 'placeholder': 'Fecha del evento'})
    )

    departamento = forms.ChoiceField(
        choices=DEPARTAMENTOS,
        label="",
        widget=forms.Select(attrs={'class': 'form-input', 'id': 'usp-custom-departamento-de-residencia',})
    )

    ciudad = forms.ChoiceField(
        choices=[],
        label="",
        widget=forms.Select(attrs={'class': 'form-input', 'id': 'usp-custom-municipio-ciudad'})
    )

    location = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Dirección'})
    )

    keynote_speaker = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Orador principal'})
    )
    image = forms.ImageField(
        label="",
        widget=forms.ClearableFileInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = JobFair
        fields = ['title', 'description', 'event_date', 'departamento', 'ciudad', 'location', 'keynote_speaker', 'image']
        help_texts = {k: "" for k in fields}

