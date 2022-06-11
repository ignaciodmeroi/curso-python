from django import forms 

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()


class ProfesionalFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    especialidad = forms.CharField(max_length=40)
    matricula = forms.IntegerField()
    email = forms.EmailField()


class AsistenteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    nempleado = forms.IntegerField()
    email = forms.EmailField()
    