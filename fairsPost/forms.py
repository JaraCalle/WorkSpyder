from django import forms
from exploreFairs.models import JobFair 

class FeriaForm(forms.ModelForm):
    class Meta:
        model = JobFair  # Usar el modelo JobFair
        fields = ['title', 'description', 'event_date', 'location', 'keynote_speaker', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
            'event_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-input'}),
            'keynote_speaker': forms.TextInput(attrs={'class': 'form-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }
