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

    nombre = models.CharField(max_length=100)
    rareza = models.IntegerField(choices=[(4, '4 estrellas'), (5, '5 estrellas')])
    elemento = models.CharField(max_length=100, choices=Elementos)
    tipo_arma = models.CharField(max_length=20)
    lore = models.TextField()
    diseno_imagen = models.ImageField(upload_to='personajes/disenos/')
    enka_api_id = models.IntegerField(help_text="ID para conectar con Enkanetwork", unique=True)

    def __str__(self):
        return self.nombre


class Build(models.Model):
    personaje = models.OneToOneField(Personaje, on_delete=models.CASCADE, related_name='build')
    arma = models.CharField(max_length=100)
    set_artefactos = models.CharField(max_length=200)
    stats_principales = models.TextField(help_text="Reloj ATQ%, Caliz Daño Elemental, Corona Daño Critico")

    def __str__(self):
        return f"Build de {self.personaje.nombre}"