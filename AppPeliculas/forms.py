from django import forms

class PeliculaFormulario(forms.Form):

    nombre = forms.CharField(max_length=10)
    año = forms.IntegerField()
    director = forms.CharField(max_length=10)
    genero = forms.CharField(max_length=10)
