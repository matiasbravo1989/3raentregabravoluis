from django.shortcuts import render
from AppPeliculas.models import *
from AppPeliculas.forms import *
# Create your views here.

def ver_pelis(request):

    todas = Pelicula.objects.all()

    return render(request, "AppPelis/verpelis.html", {"todas": todas})

def agregar_pelis(request):

    if request.method == "POST":

        miFormulario = PeliculaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                pelicula = Pelicula (nombre=informacion["nombre"], año=informacion ["año"], director=informacion["director"],
                                     genero=informacion["genero"])
                pelicula.save()
                return render(request, "AppPeliculas/verPelis.html")
    else:
        miFormulario = PeliculaFormulario ()

    return render(request, "AppPeliculas/peliFormulario.html", {"miFormulario": miFormulario})

def buscarPelis (request):

    return render(request, "AppPeliculas/buscarpelis.html")

def resultados(request):

    directorBusqueda= request.GET["director"]
    resultadosPeliculas= Pelicula.objects.filter(director__icontains=directorBusqueda)


    return render(request, "AppPeliculas/resultados.html" , {"info1":directorBusqueda, "info2":resultadosPeliculas})
