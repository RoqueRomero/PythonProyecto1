from django import forms
from .models import Estudiante

class formulario(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields=['apellido','nombres','materia','comision']
        
        
    