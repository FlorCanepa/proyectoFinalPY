# Proyecto con Django

Este es un proyecto desarrollado con Django. La aplicación permite a los usuarios ver una lista de libros publicados, con detalles como el autor, la editorial, la fecha de publicación, y la imagen de portada.
Características Principales
Autenticación de Usuarios: Los usuarios pueden registrarse e iniciar sesión.
Gestión de Libros: Los usuarios pueden agregar, editar y eliminar libros.
Visualización de Libros: Los libros publicados se muestran en una lista con su título, autor, editorial, fecha de publicación e imagen de portada.

## Requisitos

- Python 3.9.13
- Django 4.x
- Pillow (para manejar las imágenes)
- virtualenv (así es como lo ejecuto yo)

## Link al video del proyecto (sin sonido, pero se utiliza todo lo implementado)
    https://drive.google.com/file/d/1kNxCW4I6WTFh1a-Hzyi1ZtTr2kUMi3Cm/view


## Instalación

1. **Clona el repositorio:**

   git clone https://github.com/FlorCanepa/proyectoFinalPY
   cd TercerEntregaPY3

2. **Crea un entorno virtual:**
    python -m venv env(este se puede cambiar)
   En Windows:
   .\env\Scripts\Activate
   En macOS/Linux:
  source env/bin/activate

3. **Instalar las dependencias:**
     pip install -r requirements.txt

4. **Ejecutar el proyecto:**
   python manage.py runserver
Abrir navegador e ir a http://127.0.0.1:8000/

5. **Datos de superuser**
   cuenta: fr4nco
   pass: 123
   (Ingresar mediante http://127.0.0.1:8000/admin)

   PD: Mis disculpas por hacer un commit fuera de termino, estuve con gripe estos dias y no toque la PC, me falto agregar el about me porque me lo olvidé, agregar algun estilo de cards y linkear bien 2 o 3 links dentro del proyecto nada mas.
   Saludos,
   Franco.

