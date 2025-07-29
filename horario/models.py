from django.db import models
import random

# Create your models here.

class Clase(models.Model):
    TURNO_CHOICES = [
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
    ]
    
    GRUPO_CHOICES = [
        ('A', 'Grupo A'),
        ('B', 'Grupo B'),
        ('C', 'Grupo C'),
        ('D', 'Grupo D'),
    ]
    
    DIA_CHOICES = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miércoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sábado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    
    # Campos básicos
    nombre_curso = models.CharField(max_length=100)
    nombre_docente = models.CharField(max_length=100)
    grupo = models.CharField(max_length=1, choices=GRUPO_CHOICES)
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)
    
    # Horarios
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    # Días que se repite (puede ser múltiples días)
    dias_semana = models.JSONField(default=list)  # Lista de días: ['lunes', 'martes', etc.]
    
    # Color único para cada clase
    color = models.CharField(max_length=7, default='#000000')  # Formato hexadecimal
    
    # Timestamps
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Generar color aleatorio si no se especifica
        if self.color == '#000000':
            self.color = self.generar_color_aleatorio()
        super().save(*args, **kwargs)
    
    def generar_color_aleatorio(self):
        """Genera un color aleatorio en formato hexadecimal"""
        colores = [
            '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7',
            '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9',
            '#F8C471', '#82E0AA', '#F1948A', '#85C1E9', '#D7BDE2',
            '#F9E79F', '#ABEBC6', '#FAD7A0', '#D5A6BD', '#A9CCE3'
        ]
        return random.choice(colores)
    
    def __str__(self):
        return f"{self.nombre_curso} - {self.nombre_docente} ({self.grupo})"
    
    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"
        ordering = ['hora_inicio', 'nombre_curso']
