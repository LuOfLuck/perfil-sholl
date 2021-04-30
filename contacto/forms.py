from django import forms

class Contacto_forms(forms.Form):

    nombre = forms.CharField(label="Nombre", required=True)

    asunto = forms.CharField(label="Asunto", required=True)

    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea)

