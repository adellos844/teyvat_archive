from django.shortcuts import render
from .models import Personaje

def home(request):
    personajes = Personaje.objects.all()
    return render(request, 'core/base.html',{'personajes': personajes})
