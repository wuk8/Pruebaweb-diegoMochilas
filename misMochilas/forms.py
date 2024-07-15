from django import forms
from .models import contacto, Mochilas, comuna

class ContactForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ['nombre', 'rut', 'telefono', 'direccion', 'comuna', 'profesion', 'sexo', 'ocupacion', 'puesto_empresa']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-select'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto_empresa': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ServicioConsultaForm(forms.Form):
    nombre_servicio = forms.CharField(label='Nombre del Servicio', max_length=100, required=False)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'rows': 3}), required=False)
    costo = forms.DecimalField(label='Costo', max_digits=10, decimal_places=2, required=False)
    duracion = forms.CharField(label='Duración', max_length=50, required=False)
    requisitos = forms.CharField(label='Requisitos', widget=forms.Textarea(attrs={'rows': 3}), required=False)
    disponibilidad = forms.BooleanField(label='Disponibilidad', required=False)

    def clean_nombre_servicio(self):
        nombre_servicio = self.cleaned_data.get('nombre_servicio', '')
        if len(nombre_servicio) < 3 or len(nombre_servicio) > 20:
            raise forms.ValidationError('El nombre del servicio debe tener entre 3 y 20 caracteres.')
        return nombre_servicio

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion', '')
        if len(descripcion.split()) < 3 or len(descripcion.split()) > 200:
            raise forms.ValidationError('La descripción debe tener entre 3 y 200 palabras.')
        return descripcion

    def clean_costo(self):
        costo = self.cleaned_data.get('costo', None)
        if costo is not None:
            if costo < 10000:
                raise forms.ValidationError('El costo mínimo debe ser de 10,000 CLP.')
            elif costo > 100000:
                raise forms.ValidationError('El costo máximo no debe exceder los 100,000 CLP.')
        return costo

    def clean_duracion(self):
        duracion = self.cleaned_data.get('duracion', '')
        if not (duracion.isdigit() and 1 <= int(duracion) <= 100):
            raise forms.ValidationError('La duración debe estar entre 1 y 100 años.')
        return duracion

    def clean_requisitos(self):
        requisitos = self.cleaned_data.get('requisitos', '')
        if len(requisitos.split()) < 3:
            raise forms.ValidationError('Los requisitos deben tener al menos 3 palabras.')
        
        
        count = sum(1 for c in requisitos if c.isdigit() and 1 <= int(c) <= 10)
        if count < 4:
            raise forms.ValidationError('Debe incluir al menos 4 números del 1 al 10 en los requisitos.')
        
        return requisitos