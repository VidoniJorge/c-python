# Flask

Flask es un microframework que nos va a ayudar a construir aplicaciones web. El concepto de micro framework hace referencia a que busca darle al desarrollador las funcionalidades mínimas para crear su aplicación y luego él podrá extender sus funcionalidades agregando librerías.

# Referencia

* [Flask](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html)
* [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/index.html)
* [bootstrap doc](https://getbootstrap.com/docs/3.3/components)
* [Flask-wtf](https://flask-wtf.readthedocs.io/)
* [Flask-login](https://flask-login.readthedocs.io/en/latest/#how-it-works)


# Armado del entorno

## Creamos nuestro entorno virtual
```sh
python -m venv venv
```


## instalamos dependencias a utilizar

```sh
pip install flask
````

```sh
pip install flask-bootstrap
```

```sh
pip install flask-wtf
```

```sh
 pip install flask-testing
```


```sh
pip install blinker
```

```sh
pip install flask-login
```

# Primeros pasos

Creamos nuestro archivo `main.py`

```python
from flask import Flask

# Instanciamos la clase Flask con el nombre de nuestra app
app = Flask("my_app")

@app.route('/hello')
def hello():
    return "Hello word"
```

Creamos la variable de entorno `FLASK_APP` con el nombre de nuestro archivo main.

```sh
    export FLASK_APP=main.py
```

Creamos la variable de entorno `FLASK_ENV` con el valor `developmen` para configurar nuestro entorno en modo desarrollo.

```sh
    export FLASK_ENV=development
```


Corremos nuestro server

```sh
    flask run 
```

Corremos un curl para ver que nuestra app se encuentra funcionando

```sh
    curl localhost:5000/hello
```

o accedemos por cualquier browser a la url `localhost:5000/hello`.

## Correr nuestro server en mode debug

Correr nuestro server en modo debug nos permitirá:

* Ver los mensajes de error en el browser.
* Las funcionalidades de nuestro server se refrescaran de forma automática, cuando modifiquemos el código sin necesidad de reiniciarlo.

Para habilitar el modo debug vamos a crear la variable de entorno `FLASK_DEBUG` y le asignaremos el valor `1`

```sh
    export FLASK_DEBUG=1
```

## Request & Response

A la hora de trabajar con aplicaciones web una de nuestras actividades cotidianas será el manipular los request y response. 
Para poder hacer esto tendremos que importar de `flask` los módulos de `request` y `make_response`.


### Ejemplo Request

Vamos como puedo extraer de nuestro request la **ip** de nuestro cliente y retornarlo como parte de nuestra respuesta.

```python
from flask import Flask, request

app = Flask("my_app")

@app.route('/my_ip')
def example_request():
    return "Tu ip es {}"
        .format(request.remote_addr) # obtenemos la ip
```

### Ejemplo Response
Para ver como funciona los response crearemos un endpoint el cual obtendrá la ip del usuario, la cargara en las cookies y retornara al browser un redirect

```python
from flask import Flask, request, make_response, redirect

app = Flask("my_app")

@app.route('/')
def home():
    response = make_response(redirect('/ip'))
    response.set_cookie('user_ip', request.remote_addr)
    return response

@app.route('/ip')
def ip():
    return "Tu ip es {}".format(request.cookies.get('user_ip'))
```

# Templates con Jinja 2
Flask nos permite utilizar templates para que construyamos nuestra capa visual. Los template se utilizarán a través de **Jinja 2** y estos no son más que un archivo **html** que contendrán la estructura base de como mostraremos la información.

Por defecto Flask obtendrá los templates del directorio `templates` ubicado en la raíz del proyecto.

Ejemplo de la estructura del proyecto
```
Flask-proyect
|_main.py
|_ /templeate
    |__ hello.html
```

Nuestro primer template.

```html
<html>
    <body>
        <h1>
            Hola {{user_ip}}
        </h1>
    </body>
</html>
```

>> Las doble llave es la forma de acceder a las variables.

Para indicarle a nuestro endpoint que tiene que utilizar un template nos valdremos del método `render_template` el cual tiene como primer parámetro el nombre del template y luego le podremos enviar las variables que necesitemos utilizar en el mismo.

```python
from flask import Flask, request, render_template

...

@app.route('/first_template')
def first_template():
    return render_template('hello.html', user_ip=request.remote_addr)
```
## Flujo de control

### IF

```html
<html>
    {% if user_ip %}
        <h1>Hola {{user_ip}}</h1>
    {% else %}
        <a href="{{url_for('home')}}">Ir a inicio</a>
    {% endif %}
</html>
```

la expresión `{% if user_ip %}` evalúa si existe la variable `user_ip` y si existe mostramos su valor, en caso contrario se deja un link a nuestro endpoint `home` mediante la función `url_for`

### FOR

```html
<html>
   ...
   <ul>
    {% for t in todos %}
        <li>{{t}}</li>
    {% endfor %}
    </ul>
</html>
```

## Extenciones de template

Una función muy potente que nos ofrece **Jinja** es la posibilidad de crear un template a partir de otro, este mecanismo es el que se conoce como extensión de template.

> Esto nos permite entre otras cosas la reutilización de código.

Para poder hacer esto lo único que tendremos que hacer es crear nuestro template base y utilizar la instrucción `{% extends 'file name'%}` dentro del template que necesitamos reutilizar nuestro template base.

**ejemplo**

cramos nuestro template base: base.html

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>Tittle</title>
    </head>
    <body>

    </body>
</html>
```

incluimos el comportamiento de nuestro template base en el template: hello.html

```html
{% extends 'base.html'%}
...
```

## Macros

Los macros nos permite generar componentes reutilizables.

Una macro se crea utilizando la instrucción `macro`. Donde su sintaxis es `{% mocro nombre_funcion(parametros de entrada)%}`

Para ejemplificar crearemos un macro que muestre un elemento de dentro de un`li`

Creamos nuestro archivo macros.html

```html
{% macro render_todo(todo) %}
<li>Descripción: {{todo}}</li>
{% endmacro %}
```

agregamos dentro de nuestro hello.html

```html
    <!-- importamos nuestro macro -->
    {% import 'macros.html' as macros %}
    
    <ul>
    {% for t in todos %}
        <!-- lo utilizamos -->
        {{ macros.render_todo(t) }}
    {% endfor %}
    </ul>
`

## Include

Include como lo dice su nombre nos permite incluir nueva funcionalidad en nuestro template sin necesidad de extender de otro.

Para ver su funcionamiento, creamos un archivo llamado `navbar.html` el cual contendrá nuestra barra de navegación.

```html
<nav>
    <ul>
        <li><a href="{{ url_for('first_template') }}">ir a inicio</a></li>
        <li><a href="https://www.google.com" target="_blank">google</a></li>
    </ul>
</nav>

```

agregamos en nuestro `base.html`

```html
...
    <header>
        {% include 'navbar.html' %}
    </header>
```

### archivos estaticos

Por defecto los archivos estáticos se van a buscar dentro de la carpeta `static` y se utiliza la instrucción `url_for` para acceder a ellos.

Para ejemplificar su funcionamiento crearemos un llamado `main.css` dentro de la carpeta `static/css`

```css
html * {
    font-family: sans-serif;
}
img {
    max-width: 30px;
}
```

el cual importamos en nuestro `base.html`

```html
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="{{url_for('static', filename='css/main.css')}}"/>
    </head>
...
</html>
```

# Manejo de errores

Para el manejo de errores **Flask** nos provee una función llamada ErrorHabler la cual se utilizara con la anotación `@app.errorhandler` a la cual le tendremos que especificar el tipo de error que queremos manejar.

veamos como podemos manejar los errores not_found de nuestra aplicación

```python
# indicamos que error queremos capturar
@app.errorhandler(404) 
def not_found(error): 
    return render_template('404.html', error=error) # se retorna el template que se desea utilizar para notificar al usuario del problema ocurrido
```

Con la función `abort` podemos lanzar nuestros propios errores. Esto es muy útil sobre todo para el manejo de los errores http del topo 5xx.


```python
from flask import ..., abort

...
    abort(500)
```


# Session 

Para poder manipular los datos a través de la sesión del usuario lo primero que tenemos que hacer en configurar una **secret key** la cual se utiliza para encriptar los datos de la sesión, esto lo podemos hacer mediante el atributo del tipo diccionario `app.config`

```python
    from flask import ..., session # importamos session
    app.config['SECRET_KEY'] = 'MY_SECRET' # configuramos nuestro secret

    ...

    def my_ip():
        session['user_ip'] = request.remote_addr # cargamos un dato en session

        session.get('user_ip') # obtenemos un dato de session
```

# Flask-Bootstrap

Es una librería que empaqueta bootstrap y nos permite utilizar sus css y javascript.

```python
from flask_bootstrap import Bootstrap
# importamos 
from flask_bootstrap import Bootstrap

app = Flask("my_app")
bootstrap = Bootstrap(app) # lo iniciamos
```

Modificamos nuestro base.html para utilizar las facilidades que nos proporciona `Flask-Bootstrap`

```
{% extends "bootstrap/base.html" %}

{% block head %}
    {{ super() }}
    <title>{% block tittle %} Hola | {% endblock %}</title>
    <link rel="stylesheet" href="{{url_for('static', filename='css/main.css')}}"/>
{% endblock %}

{% block body %}
    {% block navbar %} {% include 'navbar.html' %} {% endblock %}
    {% block content %} {% endblock%}
{% endblock %}
```


cargamos en nuestro navbar un código
```html
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="{{ url_for('first_template') }}">
                <img src="{{ url_for('static', filename='images/platzi.png') }}" style="max-width: 48px"
                    alt="Platzi logo">
            </a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="{{ url_for('first_template') }}">Inicio</a></li>
                <li><a href="https://platzi.com" target="_blank">Platzi</a></li>
            </ul>
        </div>
    </div>
</div>
```


# Flask-WTF

Librería que nos ayuda a manejar formularios.


```python
    from flask_wtf import FlaskForm
    from wtforms.fields import StringField, PasswordField, SubmitField
    from wtforms.validators import DataRequired

    class LoginForm(FlaskForm):
        username = StringField('Nombre de usuario', validators=[DataRequired()])
        password = PasswordField('Contraseña', validators=[DataRequired()])
        submit = SubmitField('enviar')
    
    @app.route('/first_template')
    def first_template():
        login_form = LoginForm()
        context = {
            #'user_ip' : request.cookies.get('user_ip'),
            'user_ip' : session.get('user_ip'),
            'todos' : todos,
            'login_form' : login_form

        }
        return render_template('hello.html', **context)
```

Obtenemos y mostramos los datos de forma manual dentro de nuestro hello.html
```html
    <div class="container">
        <form action="{{ url_for('hello')}}" method="post">
            {{ login_form.username }}
            {{ login_form.username.label }}
        </form>
    </div>
```

Mostramos el formulario utilizando la libreria de wtf
```html
    {% import 'bootstrap/wtf.html' as wtf %}

    <div class="container">
        {{ wtf.quick_form(login_form) }}
    </div>
```

# Desplegar Flashes (mensajes emergentes)

Con la función `flash` podremos mostrar mensajes emergentes, para esto importamos está función desde flask.

Lo primero que tenemos que hacer es cargar los datos como se muestra a continuación

```python
from flask import ...flash

def my_method():
    ...
    flask('Nombre de usuario registrado con exito')
    ...
```

Lo único que nos resta hacer es mostrarlo, para eso vamos a uno de nuestros template y agregamos
un for que recorra todos los mensajes de la función `get_flashed_messages()` 

```
  {% for message in get_flashed_messages() %}
        <div class="alert alert-success alert-dismissible">
            <button type="button"
                    data-dismiss="alert"
                    class="close">&times;</button>
            {{ message }}
        </div>
    {% endfor %}
    
    {% block scripts %}
        {{ super() }}
    {% endblock %}
```

El ejemplo canterion decora el mensaje con clases de `bootstrap` y para que funcione el botón cerrar se carga los script también de `bootstrap`

# Flask-testing

```python
import unittest

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
```

# Blueprints

Flask utiliza un concepto de blueprints para crear componentes de aplicaciones y soportar patrones comunes dentro de una aplicación o entre aplicaciones. Los blueprints pueden simplificar en gran medida el funcionamiento de las grandes aplicaciones y proporcionar un medio central para que las extensiones de Flask registren operaciones en las aplicaciones. Un objeto **Blueprint** funciona de forma similar a un objeto de aplicación Flask, pero no es realmente una aplicación. Más bien es un blueprint de cómo construir o extender una aplicación.

