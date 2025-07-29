# Organizador de Horario

Un sistema web para organizar y gestionar horarios de clases desarrollado con Django.

## Características

- 📅 **Horario Visual**: Vista de horario semanal con bloques de tiempo de 5 AM a 12 AM
- 🔐 **Autenticación Segura**: Sistema de login para proteger funciones de gestión
- 🎨 **Colores Únicos**: Cada clase tiene un color distintivo automático
- 👥 **Gestión de Grupos**: Soporte para grupos A, B, C y D
- 👨‍🏫 **Información Completa**: Curso, docente, horario, días y turno
- ✏️ **CRUD Protegido**: Crear, leer, actualizar y eliminar clases (solo usuarios autenticados)
- 📱 **Responsive**: Diseño adaptativo para móviles y tablets
- 🎯 **Interfaz Moderna**: Diseño con Bootstrap 5 y iconos

## Requisitos

- Python 3.8+
- Django 5.2+

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd Organizar-Horario
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias**
   ```bash
   pip install django
   ```

5. **Configurar base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Crear usuarios adicionales (opcional)**
   ```bash
   python crear_usuario.py
   ```

8. **Ejecutar servidor**
   ```bash
   python manage.py runserver
   ```

9. **Acceder a la aplicación**
   - Aplicación principal: http://localhost:8000/
   - Panel de administración: http://localhost:8000/admin/

## Uso

### Agregar una Clase

1. Haz clic en "Agregar Clase" en la barra de navegación
2. Completa el formulario con:
   - **Nombre del Curso**: Ej. "Matemáticas I"
   - **Nombre del Docente**: Ej. "Dr. Juan Pérez"
   - **Grupo**: Selecciona A, B, C o D
   - **Turno**: Mañana o Tarde
   - **Hora de Inicio**: Ej. 08:00
   - **Hora de Fin**: Ej. 10:00
   - **Días de la Semana**: Selecciona los días que se imparte

3. Haz clic en "Crear Clase"

### Ver el Horario

- El horario se muestra automáticamente en la página principal
- Cada clase aparece en su bloque de tiempo correspondiente
- Los colores son asignados automáticamente
- Puedes ver detalles al pasar el mouse sobre cada clase

### Editar/Eliminar Clases

- Usa los botones de editar (lápiz) o eliminar (basura) en cada clase
- La edición mantiene el mismo color de la clase
- La eliminación requiere confirmación
- **Nota**: Solo usuarios autenticados pueden editar/eliminar clases

## Autenticación

### Iniciar Sesión

1. Haz clic en "Iniciar Sesión" en la barra de navegación
2. Ingresa tu nombre de usuario y contraseña
3. Haz clic en "Iniciar Sesión"

### Funciones Protegidas

- **Agregar Clase**: Solo usuarios autenticados
- **Editar Clase**: Solo usuarios autenticados
- **Eliminar Clase**: Solo usuarios autenticados
- **Ver Horario**: Acceso público para todos

### Gestión de Usuarios

El registro de usuarios está deshabilitado por seguridad. Para crear nuevos usuarios:

1. **Usando el script interactivo**:
   ```bash
   python crear_usuario.py
   ```

2. **Usando Django admin**:
   - Accede a http://localhost:8000/admin/
   - Inicia sesión con un superusuario
   - Ve a "Users" y crea nuevos usuarios

3. **Usando línea de comandos**:
   ```bash
   python manage.py createsuperuser
   ```

## Estructura del Proyecto

```
horario_organizer/
├── horario/                    # Aplicación principal
│   ├── models.py              # Modelo de datos Clase
│   ├── views.py               # Vistas de la aplicación
│   ├── forms.py               # Formularios
│   ├── admin.py               # Configuración del admin
│   ├── urls.py                # URLs de la aplicación
│   └── templates/horario/     # Plantillas HTML
│       ├── base.html          # Plantilla base
│       ├── horario.html       # Vista principal del horario
│       ├── form_clase.html    # Formulario de clases
│       └── confirmar_eliminar.html
├── horario_organizer/         # Configuración del proyecto
│   ├── settings.py            # Configuraciones de Django
│   └── urls.py                # URLs principales
├── manage.py                  # Script de gestión de Django
└── README.md                  # Este archivo
```

## Modelo de Datos

### Clase
- `nombre_curso`: Nombre del curso (CharField)
- `nombre_docente`: Nombre del docente (CharField)
- `grupo`: Grupo A, B, C o D (CharField)
- `turno`: Mañana o Tarde (CharField)
- `hora_inicio`: Hora de inicio (TimeField)
- `hora_fin`: Hora de fin (TimeField)
- `dias_semana`: Lista de días (JSONField)
- `color`: Color único de la clase (CharField)
- `fecha_creacion`: Fecha de creación (DateTimeField)
- `fecha_actualizacion`: Fecha de última actualización (DateTimeField)

## Tecnologías Utilizadas

- **Backend**: Django 5.2
- **Base de Datos**: SQLite (por defecto)
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Lenguaje**: Python 3.8+

## Características Técnicas

- **Responsive Design**: Adaptable a diferentes tamaños de pantalla
- **CRUD Operations**: Operaciones completas de base de datos
- **Form Validation**: Validación de formularios en frontend y backend
- **Color Generation**: Generación automática de colores únicos
- **Admin Interface**: Panel de administración personalizado
- **API Endpoint**: Endpoint JSON para integración con otros sistemas

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

- Proyecto: [Organizador de Horario](https://github.com/tu-usuario/organizador-horario)
- Email: tu-email@example.com

---

Desarrollado con ❤️ usando Django 