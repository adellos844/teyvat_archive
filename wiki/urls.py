from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('personaje/<int:pk>/', views.detalle_personaje, name='detalle_personaje'),
    path('personajes/', views.lista_personajes, name='lista_personajes'),
]