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

class Arma(models.Model):
    TIPOS_ARMA = [
        ('Espada', 'Espada ligera'),
        ('Mandoble', 'Mandoble'),
        ('Lanza', 'Lanza'),
        ('Arco', 'Arco'),
        ('Catalizador', 'Catalizador'),
    ]

    nombre = models.CharField(max_length=100)
    rareza = models.IntegerField(default=4)
    tipo = models.CharField(max_length=20, choices=TIPOS_ARMA)
    ataque_base = models.IntegerField()
    substat_tipo = models.CharField(max_length=50, help_text="Ej: Daño Crítico, ATQ %")
    substat_valor = models.CharField(max_length=20) 
    imagen = models.ImageField(upload_to='armas/')
    pasiva_nombre = models.CharField(max_length=100, blank=True)
    pasiva_descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Build(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE, related_name='builds')
    arma_recomendada = models.ForeignKey(Arma, on_delete=models.CASCADE)
    
    set_artefactos = models.CharField(max_length=200, help_text="Ej: 4 piezas de Sombra Verde Esmeralda")
    stats_principales = models.CharField(max_length=255, help_text="Ej: ATQ% / Pyro / Crítico")
    
    mejor_opcion = models.BooleanField(default=False)
    explicacion = models.TextField(blank=True)

    def __str__(self):
        return f"Build de {self.personaje.nombre}"
    
class Banner(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='banners/')
    activo = models.BooleanField(default=True) # Para decidir cuál mostrar y cuál ocultar
    fecha_fin = models.DateTimeField(blank=True, null=True) # Opcional: para saber cuándo termina

    def __str__(self):
        return self.nombre