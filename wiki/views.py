from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegistroForm
from .models import Arma, Banner, Personaje, Build, TeamComposition
from django.contrib.auth.decorators import login_required
from .utils import obtener_datos_enka

def home(request):
    personajes_recientes = Personaje.objects.all().order_by('-id')[:8]
    Armas_recientes = Arma.objects.all().order_by('-id')[:4]
    banners = Banner.objects.filter(activo=True)
    return render(request, 'wiki/home.html', {
        'personajes': personajes_recientes,
        'armas': Armas_recientes,
        'banners': banners,
    })

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            # Mostrar errores del formulario
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})

def detalle_personaje(request, pk):
    personaje = get_object_or_404(Personaje, pk=pk)
    builds = personaje.builds.select_related('arma_recomendada').all()
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

def lista_equipos(request):
    equipos = TeamComposition.objects.all()
    return render(request, 'wiki/lista_equipos.html', {'equipos': equipos})

def detalle_equipo(request, pk):
    equipo = get_object_or_404(TeamComposition, pk=pk)
    return render(request, 'wiki/detalle_equipo.html', {'equipo': equipo})

@login_required
def perfil_usuario(request):
    perfil = request.user.perfil
    datos_enka = obtener_datos_enka(perfil.uid_genshin)
    
    # Verificar si hay error
    error = None
    if isinstance(datos_enka, dict) and 'error' in datos_enka:
        error = datos_enka['error']
        datos_enka = None
    
    return render(request, 'wiki/perfil_usuario.html', {
        'perfil': perfil,
        'datos': datos_enka,
        'error': error,
        'uid': perfil.uid_genshin
    })