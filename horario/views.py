from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Clase
from .forms import ClaseForm
import json
from datetime import datetime, time

# Create your views here.

def horario_view(request):
    """Vista principal que muestra el horario completo"""
    clases = Clase.objects.all()
    
    # Organizar clases por día y hora
    horario_organizado = {}
    dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    
    for dia in dias:
        horario_organizado[dia] = {}
        # Crear bloques de 2 horas de 5 AM a 12 AM (10 bloques)
        for hora in range(5, 24, 2):
            horario_organizado[dia][f"{hora:02d}:00-{(hora+2):02d}:00"] = []
    
    # Llenar el horario con las clases
    for clase in clases:
        for dia in clase.dias_semana:
            if dia in horario_organizado:
                hora_inicio = clase.hora_inicio.strftime("%H:%M")
                hora_fin = clase.hora_fin.strftime("%H:%M")
                
                # Encontrar el bloque de 2 horas correspondiente
                hora_inicio_num = clase.hora_inicio.hour
                # Para bloques que empiezan en 5, 7, 9, 11, etc.
                if hora_inicio_num % 2 == 1:  # Si es impar (5, 7, 9, 11, etc.)
                    bloque_inicio = hora_inicio_num
                else:  # Si es par (6, 8, 10, 12, etc.)
                    bloque_inicio = hora_inicio_num - 1
                bloque_key = f"{bloque_inicio:02d}:00-{(bloque_inicio+2):02d}:00"
                
                # Agregar la clase al bloque correspondiente
                if bloque_key in horario_organizado[dia]:
                    horario_organizado[dia][bloque_key].append({
                        'clase': clase,
                        'hora_inicio': hora_inicio,
                        'hora_fin': hora_fin,
                        'duracion': calcular_duracion(clase.hora_inicio, clase.hora_fin)
                    })
    
    # Obtener cursos únicos disponibles (sin duplicados)
    cursos_disponibles = []
    for clase in clases:
        if clase.nombre_curso not in [c['nombre'] for c in cursos_disponibles]:
            cursos_disponibles.append({
                'nombre': clase.nombre_curso,
                'color': clase.color
            })
    
    context = {
        'horario': horario_organizado,
        'dias': dias,
        'horas': [f"{hora:02d}:00-{(hora+2):02d}:00" for hora in range(5, 24, 2)],
        'clases': clases,
        'cursos_disponibles': cursos_disponibles,
    }
    
    return render(request, 'horario/horario.html', context)

@login_required
def agregar_clase(request):
    """Vista para agregar una nueva clase"""
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            clase = form.save()
            messages.success(request, f'Clase "{clase.nombre_curso}" agregada exitosamente.')
            return redirect('horario:horario')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ClaseForm()
    
    context = {
        'form': form,
        'titulo': 'Agregar Nueva Clase'
    }
    
    return render(request, 'horario/form_clase.html', context)

@login_required
def editar_clase(request, pk):
    """Vista para editar una clase existente"""
    clase = get_object_or_404(Clase, pk=pk)
    
    if request.method == 'POST':
        form = ClaseForm(request.POST, instance=clase)
        if form.is_valid():
            clase = form.save()
            messages.success(request, f'Clase "{clase.nombre_curso}" actualizada exitosamente.')
            return redirect('horario:horario')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ClaseForm(instance=clase)
    
    context = {
        'form': form,
        'clase': clase,
        'titulo': 'Editar Clase'
    }
    
    return render(request, 'horario/form_clase.html', context)

@login_required
def eliminar_clase(request, pk):
    """Vista para eliminar una clase"""
    clase = get_object_or_404(Clase, pk=pk)
    
    if request.method == 'POST':
        nombre_clase = clase.nombre_curso
        clase.delete()
        messages.success(request, f'Clase "{nombre_clase}" eliminada exitosamente.')
        return redirect('horario:horario')
    
    context = {
        'clase': clase
    }
    
    return render(request, 'horario/confirmar_eliminar.html', context)

@csrf_exempt
def api_clases(request):
    """API para obtener clases en formato JSON"""
    if request.method == 'GET':
        clases = Clase.objects.all()
        data = []
        
        for clase in clases:
            data.append({
                'id': clase.id,
                'nombre_curso': clase.nombre_curso,
                'nombre_docente': clase.nombre_docente,
                'grupo': clase.grupo,
                'turno': clase.turno,
                'hora_inicio': clase.hora_inicio.strftime("%H:%M"),
                'hora_fin': clase.hora_fin.strftime("%H:%M"),
                'dias_semana': clase.dias_semana,
                'color': clase.color,
            })
        
        return JsonResponse({'clases': data})
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def calcular_duracion(hora_inicio, hora_fin):
    """Calcula la duración en minutos entre dos horas"""
    inicio_minutos = hora_inicio.hour * 60 + hora_inicio.minute
    fin_minutos = hora_fin.hour * 60 + hora_fin.minute
    
    if fin_minutos < inicio_minutos:
        fin_minutos += 24 * 60  # Agregar 24 horas si pasa de medianoche
    
    return fin_minutos - inicio_minutos

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect('horario:horario')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'horario/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('horario:horario')

def register_view(request):
    messages.warning(request, 'El registro de usuarios está deshabilitado. Contacta al administrador para crear una cuenta.')
    return redirect('horario:login')
