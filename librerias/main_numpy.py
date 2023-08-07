import numpy as np

def array():
    lista = np.array([1,2,3,4,5,6,7,8,9])
    print(type(lista))

    '''
    Slicing: proceso por el cual voy a seleccionar un grupo de a generar un subgrupo de valores del array.

    print(lista[1:5]) #[2 3 4 5]
    print(lista[1:5]) #[1 2 3 4 5]
    print(lista[2:])  #[3 4 5 6 7 8 9]
    print(lista[::2]) #[1 3 5 7 9]
    print(lista[-1])  #9
    '''
    print(lista[1:5])
    print(lista[:5])
    print(lista[2:])
    print(lista[::2])
    print(lista[-1])

    '''
    m = [[1,2,3],[3,4,5],[6,7,8]]
    matriz = np.array(m)
    print(matriz)
    '''

    matriz = np.array([[1,2,3],[3,4,5],[6,7,8]])
    print(matriz)

    print(np.arange(0,10)) # crea un array de con de 10 valores
    print(np.arange(0,10,2)) # crea un array hasta el valor 10, saltando sus valores de 2 en 2
    print(np.zeros(3)) # se utiliza para crear un estructura inicial, crea un array cuyos elementos están compuesto por 0
    print(np.ones(3)) # se utiliza para crear un estructura inicial, crea un array cuyos elementos están compuesto por 1
    print(np.linspace(0,10,10)) # valor de inicio, valor de fin, cuantos datos quiero generar
    print(np.eye(4)) # crea una matriz con la diagonal principal en 1 y el resto en 0
    print(np.random.rand(4)) # crea una estructura con valores aleatorios, con valores entre 0 y 1
    print(np.random.randint(1,14)) # retorna valor random entre 1 y 14
    print(np.random.randint(1,14,(10,10))) # retorna una matriz 10x10 con valores aleatorios entre 1 y 14


def tipos_datos():
    matriz = np.array([[1,2,3],[3,4,5],[6,7,8]])
    print('Tipos de datos que contiene la matriz ', matriz.dtype)
    print('Creamos un array y le asignamos un tipo a los datos que contendra ', np.array([1,2,3], dtype='float64'))
    print('Modificamos el tipo de datos al tipo floar64 ', matriz.astype(np.float64))


def dimensiones():
     # con la propiedad ndim podemos ver la cantidad de dimensiones
    print('scalar', np.array(42).ndim)
    print('vector', np.array([1,2,3]).ndim)
    print('matris', np.array([[1,2,3],[4,3,2]]).ndim)
    print('tensor', np.array([[[1,2,3],[4,3,2]],[[1,2,3],[4,3,2]]]).ndim)
    
    '''
        agregar y eliminar dimensiones
    '''
    vector = np.array([1,2,3], ndmin=10) # Creamos una colección de 10 dimensiones
    
    # con el método np.expand_dims aumentamos la cantidad de dimensiones
          
    expand = np.expand_dims(np.array([1,2,3]),axis=0) # axis sus valores representan: 0 - filas ; 1 - columnas 
    

    print(vector, vector.ndim)
    vector2 = np.squeeze(vector) # squeeze elimina las dimensiones vacías
    print(vector2, vector2.ndim)

def shape_reshape():
    arr = np.random.randint(0,10,(3,2))
    print(arr.shape) # indica la forma del arreglo.
    print(arr.reshape(1,6)) # transforma el arreglo mientras se mantengan los elementos.
    print(arr.reshape(2,3))
    print(np.reshape(arr, (2,3)) )
    print(np.reshape(arr, (2,3)),'C') # se puede hacer un reshape como lo haría C.
    print(np.reshape(arr, (2,3)),'F') # también se puede hacer reshape a como lo haría Fortran.
    print(np.reshape(arr, (2,3)),'A') # además, existe la opción de hacer reshape según como esté optimizado nuestro computador. En este caso es como en C.

def principal_functions():
    arr = np.random.randint(1,20,10)
    matriz = np.reshape(arr, (2,5))
    print(matriz)
    print("max - ", matriz.max()) # me trae el valor más grande de mi arreglo
    print("max(1) - ", matriz.max(1)) # puedo especificar el eje, 0 - es por columna; 1 - es por fila
    print("argmax - ", matriz.argmax()) # me muestra el indice del valor más grande
    print("argmax - ", matriz.argmax(1)) # me muestra el indice del valor más grande por columba o fila
    print("min - ", matriz.min()) # me trae el valor más chico de mi arreglo - tiene el mismo comportamiento que el max

    print("ptp - ", matriz.ptp()) # muestra la diferencia que tenemos entre el pico más bajo y el pico más alto
    print("ptp - ", matriz.ptp(0)) # podemos pedir lo mismo pero por 0 - es por columna; 1 - es por fila

    print("sort - ", np.sort(matriz))
    print("percentile - ", np.percentile(matriz, 50))
    print("median - ", np.median(matriz))
    print("std - ", np.std(matriz)) # desviación estandar
    print("var - ", np.var(matriz)) # varianza
    print("mean - ", np.mean(matriz)) # media

    a  = np.array([(1,2),(3,4)])
    print(a)
    b  = np.array([(5,6),(7,8)])
    print(b)
    print(np.concatenate((a,b), axis=0))






principal_functions()