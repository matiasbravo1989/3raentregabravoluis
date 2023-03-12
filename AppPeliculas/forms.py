from django import forms

from AppPeliculas.models import Estreno

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class PeliculaFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    año = forms.IntegerField()
    director = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    reseña = forms.CharField(widget=forms.Textarea)

class EstrenoFormulario(forms.ModelForm):

    class Meta:

        model = Estreno

        fields = ["nombre", "fecha", "imagen"]

class RegistroFormulario (UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:  

        model= User
        fields = ["username", "email", "password1", "password2"]
                                






                                


