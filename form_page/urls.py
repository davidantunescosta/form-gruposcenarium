from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_formulario, name='mostrar_formulario'),
    path('obrigado/', views.mostrar_obrigado, name='mostrar_obrigado')
]