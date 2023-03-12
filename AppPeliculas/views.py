from django.http import HttpResponse
from django.shortcuts import render
from AppPeliculas.forms import PeliculaFormulario, EstrenoFormulario, RegistroFormulario
from AppPeliculas.models import Pelicula, Estreno
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppPeliculas.models import *
from AppPeliculas.forms import *
# Create your views here.


def registrar(request):
    
    if request.method == "POST":
         
         form = RegistroFormulario(request.POST)

    if form.is_valid():
            
            user=form.cleaned_data["username"]
            form.save()

            return render(request, "AppPeliculas/inicio.html", {"mensaje": "Usuario Creado"})
    else: 
        form = RegistroFormulario() 

    return render (request, "AppPeliculas/Autenticar/registro.html", {"form": form })

def login_request(request):
     
     if request.method == "POST":
          
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
               
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")

            user=authenticate (username=usuario, password=contra)

            if user: 

                login(request, user)

                return render(request, "AppPeliculas/inicio.html", {"mensaje": f"Bienvenido {user}"})
            
            else: 

                return render(request, "AppPeliculas/inicio.html", {"mensaje":"Error. Datos incorrectos"})
            
        else:
             
             form =  AuthenticationForm()

        return render (request, "AppPeliculas/Autenticar/login.html", {"form": form})
     
def about(request):
     return render(request, "AppPeliculas/about.html")

@login_required
def inicio (request):
     
     return render (request, "AppPeliculas/inicio.html")

@login_required
def addreseña(request):
     
    if request.method == "POST":
           
           miformulario=PeliculaFormulario(request.POST)

           if miformulario.is_valid():

                informacion = miformulario.cleaned_data

                peli = Pelicula(autor=request.user,nombre=informacion["nombre"], año=informacion["año"],
                    director=informacion["director"], puntaje=informacion ["puntaje"], reseña=informacion["reseña"])
                
                peli.save()

                return render(request, "AppPeliculas/inicio.html")
    else: 

            miFormulario=PeliculaFormulario()

    return render(request, "AppReseñas/Reseñas/añadirReseñas.html", { "form":miFormulario})

@login_required
def buscar(request): 

    if request.GET ["reseña"]:
         
         nombre=request.GET ["reseña"]

         resultados=Pelicula.objects.filter(nombre_icontains=nombre)

         return render(request, "AppPeliculas/Reseñas/resultadosBusqueda.html", {"resultados":resultados, "busqueda":buscarPelis })

    else:

        respuesta="No enviaste datos."

    return HttpResponse(respuesta)

@login_required
def addEstrenos(request):

     if request.method == "POST":
          
        miFormulario=EstrenoFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():  

            informacion = miFormulario.cleaned_data


            Estreno = Estreno (nombre=informacion ["nombre"], fecha=informacion["fecha"],
                imagen=informacion ["imagen"])
            
            Estreno.save()
            
            return render (request, "AppReseñas/inicio.html")
        
        else: 

            miFormulario=EstrenoFormulario()

        return render(request, "AppPeliculas/Estrenos/añadirEstrenos.html", {"form":miFormulario})
     
@login_required
def borrarEstrenos(request, estreno_nombre):
     
     peli = Estreno.objects.get(nombre=estreno_nombre)

     peli.delete()

     estrenos = Estreno.objects.all()

     return render (request, "AppPeliculas/Estrenos/listaEstrenos.html", {"resultados":estrenos})

@login_required
def editarEstreno(request, estreno_nombre):
     
     peli = Estreno.objects.get(nombre=estreno_nombre)

     if request.method == "POST":
    
        miFormulario = EstrenoFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
             
            informacion = miFormulario.cleaned_data

            peli.nombre = informacion["nombre"]
            peli.fecha = informacion["fecha"]
            peli.imagen = informacion["imagen"]

            peli.save

            return render(request, "AppReseñas/inicio.html")
        
     else:

            miFormulario = EstrenoFormulario(initial={"nombre":peli.nombre, "fecha": peli.fecha,
            "imagen":peli.imagen})

            return render(request, "AppPeliculas/Estrenos/editarEstreno.html", {"miformulario": miFormulario, "resultados":Estreno})

@login_required
def editarUsuario(request):
     
     usuario = request.user

     if request.method == "POST":
          
        miformulario = RegistroFormulario(request.POST)

        if miformulario.is_valid():
               
            informacion =  miformulario.cleaned_data

            usuario.username = informacion["username"]
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password1"]
            usuario.save()
            
            return render (request, "AppPeliculas/Autenticar/inicio.html")
        
        else:

            miFormulario = RegistroFormulario(initial={"username":usuario.username, "email":usuario.email})

        return render(request, "AppPeliculas/Autenticar/editarusuario.html", {"miformulario":miformulario, "usuario":usuario})
               

def ver_pelis(request):

    todas = Pelicula.objects.all()

    return render(request, "AppPeli/verpelis.html", {"todas": todas})

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
