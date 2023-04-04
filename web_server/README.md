# Init web-server

uvicorn <nombre de nuestro archivo>:<objeto que contiene nuestra aplicacion> 
--reload bandera para que cuando se modifique algo en el codigo veamos el cambio en el navegador

```sh
uvicorn main:app --reload
```

```sh
docker-compose build
````

```sh
docker-compose up -d
```

# FastApi

El framework más veloz para el desarrollo web con Python. Fue creado por Sebastian Ramirez, es de código abierto y se encuentra en Github, es usado por empresas como Uber, Windows, Netflix y Office.


FastAPI utiliza otros frameworks dentro de si para funcionar:

* **Uvicorn**: Es una librería de Python que funciona de servidor, es decir, permite que cualquier computadora se convierta en un servidor.
* **Starlette**: Es un framework de desarrollo web de bajo nivel, para desarrollar aplicaciones con este requieres un amplio conocimiento de Python, entonces FastAPI se encarga de añadirle funcionalidades por encima para que se pueda usar mas fácilmente.
* **Pydantic**: Es un framework que permite trabajar con datos similar a pandas, pero este te permite usar modelos los cuales aprovechara FastAPI para crear la API

## Documentación

FastAPI está parado sobre los hombros de OpenAPI, el cual es un conjunto de reglas que permite definir cómo describir, crear y visualizar APIs. Es un conjunto de reglas que permiten decir que una API está bien definida.
ㅤ
FastAPI nos genera de forma automática la documentación en formato:
* swagger
* redoc

Acceder a la documentación interactiva con Swagger UI:
`{localhost}/docs`

Acceder a la documentación interactiva con Redoc:
`{localhost}/redoc`

### Tags
Podemos ordenar la documentación interactiva mediante el parámetro **tags** cuando creamos una **path operation**, al momente de definir el **path decorator**.

**Ejemplo:**

```python
@app.get("/contact", response_class=HTMLResponse, tags=["contact"])
```

### Detalle en la descripción
Podemos agregar más detalles en la descripción de nuestros **path operations** mediante los `Docstring` dentro de nuestras **path function** y el parámetro `summary` dentro de nuestros **path decorator**

**ejemplo**

```python
@app.post(
        path="/person",
        status_code=status.HTTP_201_CREATED, 
        response_model=PersonResponse, 
        tags=["person"], 
        summary="Create person in the app"
        )
def create_person(person: PersonRequest = Body(...)):
    # ... el body es obligatorio
    # Docstring
    """
        Create Person

        This path operation creates a person in the app and save the information in the database

        Parameters:
        - Request body parameter:
            - **person: Person** -> A person model with first name, last name, age hair color and marital status
        
        Returns a person model with first name, last name, age hair color and marital status
    """
    return person
```

### Deprecar
Podemos deprecar un **path operation** agregando el parámetro `deprecated=True` dentro de nuestro **path decorator**.

**ejemplo**
```python
@app.get(
    path="/person/details", 
    status_code=status.HTTP_200_OK, 
    tags=["person"],
    deprecated=True
    )
```

## Primeros pasos

```python
from fastapi import FastAPI

# Variable va a contener toda nuestra aplicación
app = FastAPI()

@app.get("/")
def home():
    return { "hello" : "world" }
```

## Path Operation

Los **path operation** es la conbinación de los path de una url + su operacion.

```python
@app.get("/")
def home():
    return { "hello" : "world" }
```

Dos conceptos asociados a los **path operation** son: 
* **Path operation decorator** : `@app.get("/")`
* **Path operation function**: `def home():`

### Path parameters

Es una parte de la url la cual puede variar, esto es muy útil para no tener que implementar un endpoint por cada combinación posible de urls.

**Ejemplo:**

Suponiendo que tenemos una API la cual nos permite consultar los datos nuestros usuarios por id, si no se dispone de los **path parameters** tendríamos que declarar una endpoint por cada id de usuario.

quedando de la siguiente manera:

* <host>/users/1
* <host>/users/2
* ....
* <host>/users/198

en su lugar gracias a los **path parameters** solo tendremos que declarar un solo endpoint

* <host>/users/{user_id}

siendo user_id una variable a la cual se le asignan los diferentes id de usuarios.

> Los **Path Parameters** son obligatorios

Para agregarle a un **Path operation** unos **Path parameter** lo que tenemos que hacer es:

1. Importar `Path` de **fastapi**.
2. Indicamos el nombre de nuestro **path parameters** en la definición de la url encerrado entre llaves --> `{}`.
3. Agregar tantos atributos en nuestra **path operation function** como **path parameters** se crearon el el paso 2.
4. A cada atributo agregado en el paso 3, le tenemos que setear el valor por defecto de la clase `Path`. Es importante saber que al momento de instancias la clase `Path` le podemos pasar por parametro las validaciones que queramos que aplique al **path parameter**.

```python
from fastapi import FastAPI, Path

...

@app.get("/person/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person id",
        description="This is the person id. It's requiered"
        )
    ):
    return { person_id : "It exists!" }
```

### Query parameters

Un Query Patameter es un conjunto de elementos opcionales los cuales son añadidos al finalizar la ruta, con el objetivo de definir contenido o acciones en la url, estos elementos se añaden despues de un **?** para agregar más query parameters utilizamos **&**

Ejemplo

> localhost/person?name=pedro&last_name=distefano

Para agregarle a un **Path operation** unos **Query parameter** lo que tenemos que hacer es:

1. Importar `Query` de **fastapi**.
2. Agregar tantos atributos en nuestra **path operation function** como **query parameters** necesitemos.
3. A cada atributo agregado en el paso 2, le tenemos que setear el valor por defecto de la clase `Query`. Es importante saber que al momento de instancias la clase `Query` le podemos pasar por parametro las validaciones que queramos que aplique al **query parameter**.

ejemplo

```python
# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel
# FastAPI
from fastapi import FastAPI, Body, Query

@app.get("/person/details")
def show_person(
    name: Optional[str] = Query(
        default=None, # Dejamos que el query parameter sea opcional y le asignamos el None como valor predeterminado
        min_length=1, max_length=50 # validaciones
        ),
    age: Optional[str] = Query(
        ... # Configuramos el query parameter como obligatorio
        )
    ):
    return { name : age }
```

**Validaciones que podemos hacer**
* Para tipos de datos str:
    * **max_length**: Para especificar el tamaño máximo de la cadena.
    * **min_length**: Para especificar el tamaño mínimo de la cadena.
    * **regex**: Para especificar expresiones regulares.

* Para tipos de datos int:
    * **ge**: (greater or equal than ≥) Para especificar que el valor debe ser mayor o igual.
    * **le**: (less or equal than ≤) Para especificar que el valor debe ser menor o igual.
    * **gt**: (greater than >) Para especificar que el valor debe ser mayor.
    * **lt**: (less than <) Para especificar que el valor debe ser menor.

**Documentación**

Es posible dotar de mayor contexto a nuestra documentación. Se deben usar los parámetros title y description.

* **title** : Para definir un título al parámetro.
* **description** : Para especificar una descripción al parámetro.

### Request body

Para configurar un endpoint que reciba un **reques body** vamos a tener que seguir los siguientes pasos:

1. Importar un la clase `BaseModel` de `pydantic`
2. Crear una clase que extienda de `BaseModel`
3. Creamos un **Path Operation** del tipo POST (o cualquier otro que método http que reciba un body)
4. Le agregamos un parámetro a nuestra **path operation function** del tipo que creamos en el paso 2

ejemplo

```python
# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel
# FastAPI
from fastapi import FastAPI, Body

...

# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None # definimos el valor por defecto por ser optional
    is_married: Optional[bool] = None

@app.post("/person")
def create_person(person: Person = Body(...)):
    # ... el body es obligatorio
    return person
```

En el ejemplo se agregaron algunas características que no son requeridas, pero si son de mucha utilidad.

Se importó la clase `Optional` de **python** para indicar que algunos atributos del body no son obligatorios.

Además importamos la clase `Body` de **fastapi** y mediante los 3 puntos especificamos que el body es obligatorio.

### Response body

Los response body también los podemos especificar y para esto solo tenemos que crear un modelo y agregarlo en nuestro **path operation decorator**. Para esto tendremos que usar el parámetro `response_model`.

```python
class PersonRequest(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., gt=0, le=150)
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)


@app.post("/person", response_model=PersonRequest)
...
```

#### Validaciones

Para agregar validaciones al **request body** vamos a tener que:

1. Importar la clase `Field` de `pydantic`
2. Modificamos nuestro modelo y le decimos que nuestros atributos vas a ser igual a un Field. `first_name: str = Field()`
3. Al momento de setear al `Field` le indicamos todas las validaciones que deseamos para ese atributo.

Ejemplo:

```python
# Python
from typing import Optional
from enum import Enum
# Pydantic
from pydantic import BaseModel, Field

...

# Models
class HairColor(Enum):
    white = "White"
    brown = "Brown"
    black = "Black"
    blonde = "Blonde"
    red = "Red"

class Location(BaseModel):
    city: str
    state: str
    country: str

class Person(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., gt=0, le=150)
    hair_color: Optional[HairColor] = Field(default=None) # definimos el valor por defecto por ser optional
    is_married: Optional[bool] = Field(default=None)

...

# Validaciones : Request Body
@app.put("/person/{person_id}")
def update_person(person_id: int = Path(...,gt=0, title="Person id", description="This is the person id. It's requiered"),
    person: Person = Body(...),
    location: Location = Body(...) # FastAPI une los 2 request body en un solo json
):
    result = person.dict()
    result.update(location.dict())
    return result

```

### Configurar ejemplos de request 

Resulta útil el poder disponibilizar en nuestra especificación de OpenAPI ejemplos de los datos que puede recibir nuestro servicio.

Para agregar estas referencias solo tenemos que agregar el atributo `example` cuando instanciamos las clases `Field`, `Query` o `Path`.

**Ejemplos:**

```python
class Location(BaseModel):
    city: str = Field(..., min_length=1, max_length=50, example="Tigre")
    state: str = Field(..., min_length=1, max_length=50, example="Buenos aires")
    country: str = Field(..., min_length=1, max_length=50, example="Argentina")

class Person(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., gt=0, le=150)
    hair_color: Optional[HairColor] = Field(default=None) # definimos el valor por defecto por ser optional
    is_married: Optional[bool] = Field(default=None)

    class Config():
        schema_extra = {
            "example": {
                "first_name" : "facundo",
                "last_name" : "Martines",
                "age": 21,
                "haid_color" : "White",
                "is_married" : False 
            }
        } 

...

@app.get("/person/details")
def show_person_details(
    name: Optional[str] = Query(
        default=None,
        min_length=1, 
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters"
        ),
    ...

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person id",
        description="This is the person id. It's requiered"
        ),
    ...
```

### Http status code

Dentro de los **path operation decorator** podemos configurar los status code que va a retornar nuestra API en caso que todo funcione bien.
Para esto solo tenemos que utilizar el parámetro `status_code` y pasar el código http.

Es de utilizad usar la clase `status` de `fastapi`, para obtener los códigos de una forma más limpia.

**ejemplo**

```python
...
from fastapi import status
...

@app.get(path='/', status_code=status.HTTP_200_OK)
def home():
...
```

### multi-part
Por defecto **fastapi** no soporta este tipo de peticiones por lo vamos a tener que instalar un paquete de python. 
Para indicar que los parámetros a recibir son del tipo de un formulario vamos a utilizar la clase `Form` de **fastapi**.

**Ejemplo:**

```python
...
from fastapi import FastAPI, Body, Query, Path, Form
...

@app.post(path="/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login(username: str = Form(...), password: str = Form(...)):
    return LoginResponse(username=username)
```

### Cookies y Headers Parameters
Si importamos las clases `Header` y `Cookie` de **fastapi** podremos manejar la recepción de header y cookies. 
La forma de hacerlo es agregando los parámetros dentro de nuestra **path function**.

**Ejemplo:**

```python
from fastapi import FastAPI, Body, Query, Path, Form, Cookie, Header
...

@app.post(path="/contact", status_code=status.HTTP_200_OK)
def contact(
    firstname: str = Form(..., max_length=20, min_length=1),
    lastname: str = Form(..., max_length=20, min_length=1),
    email: EmailStr = Form(...),
    message: str = Form(..., min_length=20),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent
...

```

### upload file
Para poder trabajar con archivos vamos a utilizar las clases `File` y `UploadFile` de **fastapi**.

Ejemplo:

```python
from fastapi import File, UploadFile
...

@app.post(path="/post-image")
def post_image(image: UploadFile = File(...)):
    return {
        "filename": image.filename,
        "format" : image.content_type,
        "size": len(image.file.read())
    }
```

### Manejo de errores

```python
from fastapi import HTTPException 
...

persons = [1,2,3,4]
@app.get("/person/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person id",
        description="This is the person id. It's requiered"
        )
    ):
    if person_id not in persons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This person doesn't exist")
    
    return { person_id : "It exists!" }
```

**Requerimiento:**
> pip install python-multipart

# Reference
* [uvicorn](https://www.uvicorn.org/)
* [fastapi](https://fastapi.tiangolo.com/)
* [pydantic: facilidades: validadores](https://docs.pydantic.dev/usage/types/#pydantic-types)

