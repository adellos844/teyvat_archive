from django.contrib import admin
from .models import Personaje, Build

@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'elemento', 'rareza', 'region')
    search_fields = ('nombre',)
    list_filter = ('elemento', 'rareza', 'region')

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('personaje', 'arma')
