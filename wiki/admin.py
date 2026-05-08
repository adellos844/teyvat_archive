from django.contrib import admin
from .models import Personaje, Arma, Build, Banner, Perfil, TeamComposition

admin.site.register(Banner)
admin.site.register(Perfil)

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
    list_display = ('personaje', 'get_categoria', 'arma_recomendada', 'mejor_opcion')
    list_filter = ('personaje', 'categoria', 'mejor_opcion')
    search_fields = ('personaje__nombre',)
    
    def get_categoria(self, obj):
        return obj.get_categoria_display()
    get_categoria.short_description = 'Categoría'

@admin.register(TeamComposition)
class TeamCompositionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dps_principal', 'dificultad')
    list_filter = ('dificultad', 'dps_principal')
    search_fields = ('nombre',)

