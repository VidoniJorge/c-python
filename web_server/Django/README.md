# Django

Es un framework que nos ayuda a crear aplicaciones web.  

**Características de Django:**
* Es rápido, no es el más rápido pero si está entre los más rapido de python
* Seguro
* Es un framework escalable

## requisitos

```sh
    pip install django
```

## Primeros pasos

Lo primero que tenemos que hacer es crear nuestro proyecto utilizando django con el comando

```sh
    django-admin startproject <nombre del proyecto>
```

Al finalizar la ejecución del comando, Django nos habrá creado la estructura básica de nuestra aplicación.

* una carpeta con el nombre del proyecto
    * __init__.py: archivo clasico de python que nos indica que estamos dentro de un paquete
    * asgi.py: nos ayuda a realizar el deploy 
    * settings.py: Contiene toda la información de la configuración de nuestro proyecto
    * urls.py: Es el archivo donde vamos a colocar las url de nuestro proyecto.
    * wsgi.py: nos ayuda a realizar el deploy 
* manage.py: se ubica en la carpeta raiz donde corrimos el comando `startproject`

Creado nuestro proyecto, vamos a comprobar que todo esté funcionando de forma correcta iniciando nuestro server de Django con el siguiente comando

```sh
    python3.10 manage.py runserver
```

tras correr el comando vamos a entrar a **localhost:8000** con algún browser y sí todo salió bien tendríamos que ver una página similar a la siguiente

![](./img/djongo_init.png)

> el puerto 8000 nos fue indicado por django cuando iniciamos el server con el mensaje --> Starting development server at http://127.0.0.1:8000/



### proyectos vs apps

Django maneja los términos proyecto y apps como 2 cosas distintas, siendo un **proyecto** un conjunto de apps y una **app* un módulo dentro de un proyecto el cual sí lo definimos de forma correcta es una pieza de código que podremos reutilizar en cualquier proyecto.

**Forma de crear una app**

```sh
    python3.10 manage.py startapp polls
```

Estructura de archivos de nuestra app

* __init__.py
* admin.py
* apps.py
* models.py
* test.py
* view.py
* urls.py: Esté archivo no lo crea el comando ejecutado, pero es conveniente que lo creemos de forma manual sí nuestra app va a manejar componentes visuales


Llegado a este punto ya tenemos creado nuestro primer proyecto y le hemos creado al mismo su primer app. Es hora de que creemos nuestro primer `hola mundo`, el cual lo haremos en la app creara.

Para esto tenemos que hacer 2 cosas:
* Crear nuestra función que nos retorne nuestro mensaje
* Exponer nuestra url

Vamos a nuestro archivo `polls/views.py` para crear nuestra función

```python
from django.shortcuts import render

# importamos HttpResponse para poder manejar la respuesta http
from django.http import HttpResponse

# creamos nuestra función index que nos retornara nuestro hola mundo
def index(request):
    return HttpResponse("hola mundo")
```

Creada la función queda exponerla en una url, para esto tendremos que modificar 2 archivos `urls.py`el de nuestro proyecto y el de nuestra app.

**polls/urls.py**: configuramos nuestro nueva url

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index") # asociamos nuestro método a un path
]
```

**urls.py**: le indicamos al proyecto que incluya las url de nuestra app

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include("polls.urls")), # incluimos las url de nuestra app polls
]
```

### settings.py



