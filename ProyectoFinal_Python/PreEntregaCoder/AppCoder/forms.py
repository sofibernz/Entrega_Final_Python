from django import forms


class ConsultasFormulario(forms.Form):

    consulta = forms.CharField(max_length=150)
    nombre = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    email = forms.EmailField()