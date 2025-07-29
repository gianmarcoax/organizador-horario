from django.contrib import admin
from .models import Clase

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ['nombre_curso', 'nombre_docente', 'grupo', 'turno', 'hora_inicio', 'hora_fin', 'dias_semana_display', 'color_display']
    list_filter = ['grupo', 'turno', 'dias_semana']
    search_fields = ['nombre_curso', 'nombre_docente']
    ordering = ['hora_inicio', 'nombre_curso']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre_curso', 'nombre_docente', 'grupo', 'turno')
        }),
        ('Horario', {
            'fields': ('hora_inicio', 'hora_fin', 'dias_semana')
        }),
        ('Apariencia', {
            'fields': ('color',),
            'classes': ('collapse',)
        }),
    )
    
    def dias_semana_display(self, obj):
        """Muestra los días de la semana de forma legible"""
        if obj.dias_semana:
            return ', '.join([dia.title() for dia in obj.dias_semana])
        return '-'
    dias_semana_display.short_description = 'Días'
    
    def color_display(self, obj):
        """Muestra el color como un cuadrado de color"""
        return f'<div style="width: 20px; height: 20px; background-color: {obj.color}; border-radius: 3px;"></div>'
    color_display.short_description = 'Color'
    color_display.allow_tags = True
