from django.contrib import admin
from .models import Personaje, Arma ,Build, Banner

admin.site.register(Banner)

@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'elemento', 'rareza', 'region')
    search_fields = ('nombre',)
    list_filter = ('elemento', 'rareza', 'region')

@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'rareza', 'ataque_base')
    list_filter = ('tipo', 'rareza')
    search_fields = ('nombre',)

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('personaje', 'arma_recomendada', 'mejor_opcion')
    list_filter = ('personaje', 'mejor_opcion')
