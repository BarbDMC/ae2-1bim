# ae1-2bim

## Actividad: Aplique los conceptos de Django para crear aplicaciones web haciendo uso de la interfaz administrativa, vistas y templates - AE1

Este proyecto es una aplicación web desarrollada con **Python**, **Django** y **SQLite**, que permite gestionar entidades relacionadas con el ecoturismo. Está centrado en tres entidades principales:

- **Parques Naturales**: Nombre, ubicación, área total.
- **Guías Turísticos**: Identificación, nombre, experiencia y asociación a un parque.
- **Recorridos**: Nombre del recorrido, duración, costo y guía asignado.

Se incluyen funcionalidades de administración a través del panel de Django, vistas para crear y listar datos, y uso de herencia de plantillas para mantener una estructura clara y reutilizable.

---

## 🗂️ Estructura del Proyecto

```bash
turismo /   
├── db.sqlite3  
├── manage.py # Script principal para correr comandos  
├── turismo/ # Proyecto Django principal  
│ ├── __init__.py  
│ ├── asgi.py   
│ ├── settings.py   
│ ├── urls.py   
│ ├── wsgi.py   
├── parque/ # Aplicación Django  
│ ├── __init__.py  
│ ├── admin.py  
│ ├── apps.py 
│ ├── forms.py # Formularios para CRUD  
│ ├── models.py # Modelos: Parque, Guía, Recorrido   
│ ├── tests.py 
│ ├── urls.py # Rutas de la app  
│ ├── views.py # Vistas basadas en funciones    
│ └── templates/parque/ # Plantillas HTML   
│ ├── base.html  
│ ├── formulario.html   
│ ├── listar_parques.html   
│ ├── listar_guias.html  
│ └── listar_recorridos.html     
│ └── migrations/   
│ ├── 0001_initial.py # Crea estructura de la BD  
│ ├── 0002_datos_iniciales.py # Precarga registros iniciales    
│  .gitignore
```  
     
## ⚙️ Inicializar entorno virtual (venv)

### 1. Crear entorno virtual:

```bash
cd turismo
python -m venv venv
```

### 2. Activar entorno virtual:

- En Windows:
```bash
venv\Scripts\activate
```
- En macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Instalar dependencias:
```bash
pip install django
```

## 📦 Ejecutar migraciones (estructura de la base de datos)

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🚀 Levantar la aplicación

```bash
python manage.py runserver
```

Accede a la app en: http://localhost:8000/parques

## 🧑‍💻 Credenciales del superusuario (desarrollo)

Accede a la la interfaz de administración de la aplicación de Django: http://localhost:8000/admin

- Usuario: admin
- Contraseña: admin
