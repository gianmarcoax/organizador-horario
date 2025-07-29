#!/usr/bin/env python
"""
Script para crear usuarios en el sistema de horarios.
Uso: python crear_usuario.py
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horario_organizer.settings')
django.setup()

from django.contrib.auth.models import User
from django.core.management import execute_from_command_line

def crear_usuario():
    print("=== CREADOR DE USUARIOS - ORGANIZADOR DE HORARIO ===\n")
    
    while True:
        print("Opciones:")
        print("1. Crear usuario normal")
        print("2. Crear superusuario")
        print("3. Listar usuarios existentes")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            crear_usuario_normal()
        elif opcion == "2":
            crear_superusuario()
        elif opcion == "3":
            listar_usuarios()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.\n")

def crear_usuario_normal():
    print("\n--- CREAR USUARIO NORMAL ---")
    
    username = input("Nombre de usuario: ").strip()
    if not username:
        print("El nombre de usuario no puede estar vacío.\n")
        return
    
    # Verificar si el usuario ya existe
    if User.objects.filter(username=username).exists():
        print(f"El usuario '{username}' ya existe.\n")
        return
    
    email = input("Email (opcional): ").strip()
    password = input("Contraseña: ").strip()
    confirm_password = input("Confirmar contraseña: ").strip()
    
    if not password:
        print("La contraseña no puede estar vacía.\n")
        return
    
    if password != confirm_password:
        print("Las contraseñas no coinciden.\n")
        return
    
    try:
        user = User.objects.create_user(
            username=username,
            email=email if email else "",
            password=password
        )
        print(f"\n✅ Usuario '{username}' creado exitosamente!")
        print(f"   - Usuario: {user.username}")
        print(f"   - Email: {user.email or 'No especificado'}")
        print(f"   - Es superusuario: {user.is_superuser}")
        print(f"   - Es staff: {user.is_staff}\n")
    except Exception as e:
        print(f"❌ Error al crear el usuario: {e}\n")

def crear_superusuario():
    print("\n--- CREAR SUPERUSUARIO ---")
    
    username = input("Nombre de usuario: ").strip()
    if not username:
        print("El nombre de usuario no puede estar vacío.\n")
        return
    
    # Verificar si el usuario ya existe
    if User.objects.filter(username=username).exists():
        print(f"El usuario '{username}' ya existe.\n")
        return
    
    email = input("Email: ").strip()
    password = input("Contraseña: ").strip()
    confirm_password = input("Confirmar contraseña: ").strip()
    
    if not password:
        print("La contraseña no puede estar vacía.\n")
        return
    
    if password != confirm_password:
        print("Las contraseñas no coinciden.\n")
        return
    
    try:
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"\n✅ Superusuario '{username}' creado exitosamente!")
        print(f"   - Usuario: {user.username}")
        print(f"   - Email: {user.email}")
        print(f"   - Es superusuario: {user.is_superuser}")
        print(f"   - Es staff: {user.is_staff}\n")
    except Exception as e:
        print(f"❌ Error al crear el superusuario: {e}\n")

def listar_usuarios():
    print("\n--- USUARIOS EXISTENTES ---")
    
    usuarios = User.objects.all().order_by('date_joined')
    
    if not usuarios:
        print("No hay usuarios registrados.\n")
        return
    
    print(f"{'Usuario':<15} {'Email':<25} {'Superuser':<10} {'Staff':<8} {'Fecha Creación'}")
    print("-" * 80)
    
    for usuario in usuarios:
        superuser = "Sí" if usuario.is_superuser else "No"
        staff = "Sí" if usuario.is_staff else "No"
        fecha = usuario.date_joined.strftime("%d/%m/%Y")
        email = usuario.email[:24] + "..." if len(usuario.email) > 25 else usuario.email
        
        print(f"{usuario.username:<15} {email:<25} {superuser:<10} {staff:<8} {fecha}")
    
    print(f"\nTotal: {usuarios.count()} usuario(s)\n")

if __name__ == "__main__":
    crear_usuario() 