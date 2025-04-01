from django.db import models
from django.contrib.auth.models import User

class Clase(models.Model):
    nombre = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    dia_semana = models.CharField(
        max_length=10, 
        choices=[
            ("Lunes", "Lunes"), ("Martes", "Martes"), ("Miércoles", "Miércoles"),
            ("Jueves", "Jueves"), ("Viernes", "Viernes"), ("Sábado", "Sábado"), ("Domingo", "Domingo")
        ]
    )
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    def __str__(self):
        return f"{self.nombre} ({self.dia_semana})"

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    IMPORTANCIA_CHOICES = [
        ("baja", "Baja"),
        ("media", "Media"),
        ("alta", "Alta"),
        ("urgente", "Urgente"),
    ]

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_limite = models.DateTimeField(null=True, blank=True)
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True, blank=True)
    clase = models.ForeignKey(Clase, on_delete=models.SET_NULL, null=True, blank=True)
    importancia = models.CharField(max_length=10, choices=IMPORTANCIA_CHOICES, default="media")

    def __str__(self):
        return self.nombre
