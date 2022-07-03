from django.contrib import admin
from django.urls import path
    
    
from mi_app.views import listar_cursos,mostrar_index, saludar_a, saludo_personalizado

urlpatterns = [
    
    path('mi_pagina/', mostrar_index),
    path('saludando/persona/<nombre>',saludar_a ),
    path('saludando-personalizado/',saludo_personalizado),
    path('listar-cursos/',listar_cursos),
]