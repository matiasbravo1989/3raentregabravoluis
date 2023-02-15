from django.urls import path
from AppPeliculas.views import *

urlpatterns = [
    path("verPelis/", ver_pelis),
    path("nuevaPeli/", agregar_pelis),

    path("buscarPeli/", buscarPelis),
    path("resultados/", resultados)
]