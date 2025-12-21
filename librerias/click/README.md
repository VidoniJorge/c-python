# Click

Click es un paquete de Python para crear interfaces de línea de comandos. Su objetivo es hacer que el proceso de escritura de herramientas de línea de comandos sea rápido.

Los 3 puntos claves de click
* anidamiento arbitrario de comandos
* generación automática de página de ayuda
* admite la carga diferida de subcomandos en tiempo de ejecución

## Referencias 
* [click docu](https://click.palletsprojects.com/)

## Instalación

```sh
    pip install click
```

## Conceptos básicos

### Crando una lina de comando

Click se base en decoraciones y para transformar un metodo en de python en una funcion de linea de comando en su caso más simple es agregando la decocoracion `@click.command()`

```python
import click

@click.command()
def hello():
    click.echo('Hello World!')

if __name__ == '__main__':
    hello()    
```

al ejecutar nuestro programa desde la terminal con `python hello.py` veremos que se imprime el mensaje `Hello World!`. 
Hasta aca no hay nada nuevo. Pero si corremos en la terminal la siguiente instrucción `python hello.py --help` vememos

```
Usage: hello.py [OPTIONS]

Options:
  --help  Show this message and exit
```````

### Comandos anidados

Si queremos crear varias una linea de comando de acapte varias opciones podemos utilizar el anidamiento de comandos y para esto utilizamos la anotación `@click.group()`

```python
@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)
```

otra forma de hacer lo mismo es 

```python
@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')
```

donde se remplaza el comando `cli.add_command(initdb)` por la anotación `@cli.command()`

## Agregando parametros

para algegar parametros utilizaremos 2 decoraciones `option()` y  `argument()`.

```python
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")
```

donde su help es 

```
>> python hello.py --help
Usage: hello.py [OPTIONS] NAME

Options:
  --count INTEGER  number of greetings
  --help           Show this message and exit.
``````


