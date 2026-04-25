from django.db import models

class Personaje(models.Model):
    Elementos = [
        ('Anemo', 'Anemo'),
        ('Geo', 'Geo'),
        ('Electro', 'Electro'),
        ('Pyro', 'Pyro'),
        ('Hydro', 'Hydro'),
        ('Cryo', 'Cryo'),
        ('Dendro', 'Dendro')
    ]
    Regiones = [
        ('Mondstadt', 'Mondstadt'), ('Liyue', 'Liyue'), ('Inazuma', 'Inazuma'),
        ('Sumeru', 'Sumeru'), ('Fontaine', 'Fontaine'), ('Natlan', 'Natlan'), ('Snezhnaya', 'Snezhnaya'),
    ]
    TIPOS_ARMA = [
        ('Espada', 'Espada ligera'), ('Mandoble', 'Mandoble'), 
        ('Lanza', 'Lanza'), ('Arco', 'Arco'), ('Catalizador', 'Catalizador'),
    ]
    nombre = models.CharField(max_length=100)
    rareza = models.IntegerField(choices=[(4, '4 estrellas'), (5, '5 estrellas')])
    elemento = models.CharField(max_length=100, choices=Elementos)
    tipo_arma = models.CharField(max_length=20, choices=TIPOS_ARMA, default='Espada')
    lore = models.TextField()
    diseno_imagen = models.ImageField(upload_to='personajes/disenos/')
    region = models.CharField(max_length=20, choices=Regiones, default='Mondstadt')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Build(models.Model):
    personaje = models.OneToOneField(Personaje, on_delete=models.CASCADE, related_name='build')
    arma = models.CharField(max_length=100)
    set_artefactos = models.CharField(max_length=200)
    stats_principales = models.TextField(help_text="Reloj ATQ%, Caliz Daño Elemental, Corona Daño Critico")

    def __str__(self):
        return f"Build de {self.personaje.nombre}"