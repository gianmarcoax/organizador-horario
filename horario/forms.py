from django import forms
from .models import Clase

class ClaseForm(forms.ModelForm):
    # Campo personalizado para los días de la semana
    dias_semana = forms.MultipleChoiceField(
        choices=Clase.DIA_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Selecciona los días en que se imparte esta clase"
    )
    
    # Campo personalizado para la hora de inicio
    hora_inicio = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        help_text="Hora de inicio de la clase"
    )
    
    # Campo personalizado para la hora de fin
    hora_fin = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        help_text="Hora de fin de la clase"
    )
    
    class Meta:
        model = Clase
        fields = [
            'nombre_curso',
            'nombre_docente',
            'grupo',
            'turno',
            'hora_inicio',
            'hora_fin',
            'dias_semana',
        ]
        widgets = {
            'nombre_curso': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Matemáticas I'
            }),
            'nombre_docente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Dr. Juan Pérez'
            }),
            'grupo': forms.Select(attrs={
                'class': 'form-control'
            }),
            'turno': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'nombre_curso': 'Nombre del Curso',
            'nombre_docente': 'Nombre del Docente',
            'grupo': 'Grupo',
            'turno': 'Turno',
            'hora_inicio': 'Hora de Inicio',
            'hora_fin': 'Hora de Fin',
            'dias_semana': 'Días de la Semana',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fin = cleaned_data.get('hora_fin')
        
        if hora_inicio and hora_fin:
            if hora_inicio >= hora_fin:
                raise forms.ValidationError(
                    "La hora de fin debe ser posterior a la hora de inicio."
                )
        
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si estamos editando una clase existente, convertir la lista JSON a choices
        if self.instance and self.instance.pk:
            if self.instance.dias_semana:
                self.initial['dias_semana'] = self.instance.dias_semana 