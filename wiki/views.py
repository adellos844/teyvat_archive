from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Arma, Banner, Personaje

def home(request):
    personajes_recientes = Personaje.objects.all().order_by('-id')[:4]
    Armas_recientes = Arma.objects.all().order_by('-id')[:4]
    banners = Banner.objects.filter(activo=True)
    return render(request, 'wiki/home.html', {
        'personajes': personajes_recientes,
        'armas': Armas_recientes,
        'banners': banners,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def detalle_personaje(request, pk):
    personaje = get_object_or_404(Personaje, pk=pk)
    builds = personaje.builds.all() 
    return render(request, 'wiki/detalle_personaje.html', {
        'personaje': personaje,
        'builds': builds
    })

def lista_personajes(request):
    todos = Personaje.objects.all().order_by('nombre') 
    return render(request, 'wiki/lista_personajes.html', {'personajes': todos})

def lista_armas(request):
    armas = Arma.objects.all().order_by('-rareza', 'nombre')
    return render(request, 'wiki/lista_armas.html', {'armas': armas})