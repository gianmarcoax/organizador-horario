#!/usr/bin/env python
"""
Script para automatizar el despliegue del organizador de horario.
Uso: python deploy.py
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Ejecuta un comando y maneja errores"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completado")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}: {e}")
        print(f"Error: {e.stderr}")
        return None

def check_git():
    """Verifica si git está instalado y configurado"""
    print("🔍 Verificando Git...")
    
    # Verificar si git está instalado
    if run_command("git --version", "Verificando instalación de Git") is None:
        print("❌ Git no está instalado. Por favor instala Git primero.")
        return False
    
    # Verificar si es un repositorio git
    if not os.path.exists(".git"):
        print("📁 Inicializando repositorio Git...")
        if run_command("git init", "Inicializando Git") is None:
            return False
    
    return True

def prepare_deployment():
    """Prepara el proyecto para despliegue"""
    print("\n🚀 PREPARANDO DESPLIEGUE")
    print("=" * 50)
    
    # Verificar Git
    if not check_git():
        return False
    
    # Instalar dependencias de producción
    print("\n📦 Instalando dependencias de producción...")
    if run_command("pip install -r requirements.txt", "Instalando dependencias") is None:
        return False
    
    # Recolectar archivos estáticos
    if run_command("python manage.py collectstatic --noinput", "Recolectando archivos estáticos") is None:
        return False
    
    # Hacer migraciones
    if run_command("python manage.py makemigrations", "Creando migraciones") is None:
        return False
    
    if run_command("python manage.py migrate", "Aplicando migraciones") is None:
        return False
    
    return True

def git_deploy():
    """Configura Git para despliegue"""
    print("\n📤 CONFIGURANDO GIT PARA DESPLIEGUE")
    print("=" * 50)
    
    # Agregar archivos
    if run_command("git add .", "Agregando archivos a Git") is None:
        return False
    
    # Commit inicial
    if run_command('git commit -m "Despliegue inicial del organizador de horario"', "Haciendo commit inicial") is None:
        return False
    
    print("\n✅ Proyecto preparado para despliegue!")
    return True

def show_deployment_instructions():
    """Muestra las instrucciones de despliegue"""
    print("\n" + "=" * 60)
    print("🎯 INSTRUCCIONES DE DESPLIEGUE")
    print("=" * 60)
    
    print("\n📋 PASOS PARA DESPLEGAR EN RAILWAY:")
    print("1. Ve a https://railway.app/")
    print("2. Inicia sesión con tu cuenta de GitHub")
    print("3. Haz clic en 'New Project'")
    print("4. Selecciona 'Deploy from GitHub repo'")
    print("5. Conecta tu repositorio de GitHub")
    print("6. Railway detectará automáticamente que es un proyecto Django")
    print("7. Configura las variables de entorno:")
    print("   - SECRET_KEY: (Railway lo genera automáticamente)")
    print("   - DEBUG: False")
    print("   - ALLOWED_HOSTS: tu-dominio.railway.app")
    print("8. Haz clic en 'Deploy Now'")
    
    print("\n📋 PASOS PARA DESPLEGAR EN RENDER:")
    print("1. Ve a https://render.com/")
    print("2. Inicia sesión con tu cuenta de GitHub")
    print("3. Haz clic en 'New +' y selecciona 'Web Service'")
    print("4. Conecta tu repositorio de GitHub")
    print("5. Configura el servicio:")
    print("   - Name: organizador-horario")
    print("   - Environment: Python 3")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: gunicorn horario_organizer.wsgi:application")
    print("6. Configura las variables de entorno:")
    print("   - SECRET_KEY: (genera una clave segura)")
    print("   - DEBUG: False")
    print("   - ALLOWED_HOSTS: tu-app.onrender.com")
    print("7. Haz clic en 'Create Web Service'")
    
    print("\n📋 PASOS PARA DESPLEGAR EN HEROKU:")
    print("1. Instala Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli")
    print("2. Ejecuta: heroku login")
    print("3. Ejecuta: heroku create tu-app-name")
    print("4. Ejecuta: git push heroku main")
    print("5. Ejecuta: heroku run python manage.py migrate")
    print("6. Ejecuta: heroku run python manage.py createsuperuser")
    
    print("\n🔧 COMANDOS ÚTILES:")
    print("- Ver logs: heroku logs --tail")
    print("- Abrir app: heroku open")
    print("- Ejecutar comando: heroku run python manage.py shell")

def main():
    """Función principal"""
    print("🚀 ORGANIZADOR DE HORARIO - DESPLIEGUE")
    print("=" * 50)
    
    # Preparar despliegue
    if not prepare_deployment():
        print("\n❌ Error al preparar el despliegue")
        return
    
    # Configurar Git
    if not git_deploy():
        print("\n❌ Error al configurar Git")
        return
    
    # Mostrar instrucciones
    show_deployment_instructions()
    
    print("\n🎉 ¡Proyecto listo para desplegar!")
    print("Sigue las instrucciones arriba para completar el despliegue.")

if __name__ == "__main__":
    main() 