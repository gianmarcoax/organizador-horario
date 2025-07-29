#!/usr/bin/env python
"""
Script para configurar Railway con la base de datos local.
Ejecutar en la terminal de Railway.
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horario_organizer.settings')
django.setup()

from django.core.management import execute_from_command_line

def setup_railway():
    """Configura Railway con la base de datos local"""
    print("🚀 CONFIGURANDO RAILWAY CON BASE DE DATOS LOCAL")
    print("=" * 50)
    
    try:
        # 1. Ejecutar migraciones
        print("\n📦 Ejecutando migraciones...")
        execute_from_command_line(['manage.py', 'migrate'])
        print("✅ Migraciones completadas")
        
        # 2. Cargar datos de backup
        print("\n📥 Cargando datos de backup...")
        execute_from_command_line(['manage.py', 'loaddata', 'db_backup.json'])
        print("✅ Datos cargados exitosamente")
        
        # 3. Verificar datos
        print("\n🔍 Verificando datos...")
        from horario.models import Clase
        clases_count = Clase.objects.count()
        print(f"✅ {clases_count} clases cargadas")
        
        # 4. Mostrar resumen
        print("\n📊 RESUMEN:")
        print(f"   - Clases cargadas: {clases_count}")
        print(f"   - Cursos únicos: {Clase.objects.values('nombre_curso').distinct().count()}")
        print(f"   - Grupos: {Clase.objects.values('grupo').distinct().count()}")
        
        print("\n🎉 ¡Railway configurado exitosamente!")
        print("🌐 Tu aplicación está lista en: https://web-production-1763c.up.railway.app/")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    setup_railway() 