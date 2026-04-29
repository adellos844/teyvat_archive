from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('personaje/<int:pk>/', views.detalle_personaje, name='detalle_personaje'),
    path('personajes/', views.lista_personajes, name='lista_personajes'),
    path('armas/', views.lista_armas, name='lista_armas'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)