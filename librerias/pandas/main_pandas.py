import pandas as pd
import numpy as np


def create_series():
    print(pd.Series(['Navas', 'Mbappe','Neymar','Messu']))

    psg_players = pd.Series(['Navas', 'Mbappe','Neymar','Messu'],
            index=[1,7,10,30])

    print(psg_players)

    dict = {1:'Navas', 7:'Mbappe',10:'Neymar',30:'Messu'}

    print(pd.Series(dict))

def create_dataframe():
    dict = {'jugador':['Navas', 'Mbappe','Neymar','Messu'],
    'altura':[183.0,170.0,170.2,165.0],
    'goles':[2,200,230,500]
    }

    df_players = pd.DataFrame(dict,index=[1,7,10,30])
    print(df_players)
    print(df_players.columns)
    print(df_players.index)
    print(df_players['jugador'][7])

def read_csv():
    df_csv = pd.read_csv('./librerias/pandas/bestsellers-with-categories.csv',
                         sep=',',
                         header=0, # None se utiliza cuando nuestro csv no tiene header
                         names=['Name', 'Author', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'] # puedo cambiar el valor de los headers
                         )  
    print(df_csv)
    return df_csv



def read_json():
    df_json = pd.read_json('./librerias/pandas/hpcharactersdataraw.json',
                           typ='Series')
    print(df_json)
                          
def loc_iloc():
    df = read_csv()

    print(df[0:4])
    print(df['Name'])
    print(df[['Name','Author', 'Year']])

    # Loc - funciona por label
    df.loc[0:4] # incluye la posicion 4
    df.loc[0:4, ['Name','Author', 'Year']] # filtro por label
    print(df.loc[:, ['Reviews']] * -1) 
    print(df.loc[:, ['Author']] == 'JJ Smith') 

    # iLoc -- funciona por indice
    print(df.iloc[:,0:3]) # trae solo las 3 columnas
    print(df.iloc[:2,2:]) # traigo las 2 primeras filas y de la segunda columna a la ultima

def add_data():
    df = read_csv()
    print(df.head(2)) # Limito a que solo me traiga 2 filas

    df['Nueva columna'] = np.nan
    print(df.head(2))
    print(df.shape[0]) # me indica la cantidad de filas que tenemos
    data = np.arange(0, df.shape[0]) # armamo un lista con valores desde 0 a la cantidad de filas
    df['Rango'] = data
    print(df.head(2))


def remove_data():
    df = read_csv()
    print(df.head(2)) # Limito a que solo me traiga 2 filas
    
    # Eliminar Columnas
    print(df.drop('Genre', axis=1).head(2)) # Elimino la columna Gener, se utiliza el axis para indicar que el drop es por columna.
    df.drop('Genre', axis=1, inplace=True) # inplace: su valor por defecto es false. Con inplace en true indicamos que queremos que elimine la columna del dataset, con el valor de inplace en false solo lo elimina en la salida.
    print(df.head(2)) 
    df.drop(0, axis=0, inplace=True) # elimino la fila 0
    print(df.head(2)) 
    df.drop([1,2], axis=0, inplace=True) # elimino la fila 1,2
    print(df.head(2)) 

def manejo_nulos():
    dict = {'col1':[1,2,3,np.nan],
            'col2':[4,np.nan,6,8],
            'col3':['a','b','c',np.nan]}
    df = pd.DataFrame(dict)
    print(df)
    print(df.isnull()) # me que valor de data frame es null
    print(df.isnull() * 1) # convierte los false en o y los true en 1 
    print(df.fillna('Missing')) # cambia los nulos por el valor que ingresamos
    print(df.interpolate()) # hace una interpolación de una serie y da un valor que el calcula, solo sirve para valores numéricos y es útil cuando nuestros datos siguen una estructura de una serie
    print(df.dropna()) # elimino los datos en null

def filtrado_por_condiciones():
    df = read_csv()
    df.head(2)

    mayor_2016 = df['Year'] > 2016 # Muestra el dataFrame con valores booleanos. True para libros tiene fecha de publicación mayor a 2016.
    genere_fiction = df['Genre'] == 'Fiction' # Muestra el dataFrame con valores booleanos. True para libros de tipo Fiction.
    print(df[mayor_2016 & genere_fiction]) # Filtra los libros que sean de tipo Fiction y que hayan sido publicado desde 2017. 
    print(df[~mayor_2016]) # Filtra los libros publicados antes o igual al 2016.
    
def principal_function():
    df = read_csv()
    print(df.info()) # Nos proporciona data importante de nuestro dataset, como el nombre de nuestras columnas, la cantidad de null por columna, el tipo de datos y su indice.
    print(df.describe()) # De las columnas numéricas nos van a dar algunos datos estadísticos.
    print(df.tail()) # Muestra los últimos 5 registros.
    print(df.memory_usage(deep=True)) # Me dice cuanta memoria estamos usando en el dataset.
    print(df['Author'].value_counts()) # Muestra cuántos datos hay de cada autor.
    print(df.drop_duplicates()) # Elimina las filas duplicadas.
    print(df.drop_duplicates(keep='last')) # Elimina las filas duplicadas menos el ultimo.
    print(df.sort_values('Year')) # Ordena los valores de menor a mayor según el año.
    print(df.sort_values('Year', ascending=False)) # Ordena los valores de mayor a menor según el año.

def groupby():
    df = read_csv()
    print(df.groupby('Author').count()) # Agrupar por Author y mostrar el conteo de los datos de las demás columnas. 
    print(df.groupby(['Author','Year']).count()) # Agrupo por 2 columnas. 
    print(df.groupby('Author').count().reset_index()) # Vuelvo a dejar la columna de Author como una columna. 
    print(df.groupby('Author').sum().loc['William Davis']) # Del resultado de la agrupación, filtro por el Author WIlliam Davis. 
    print(df.groupby('Author').agg(['min','max'])) # Agrupado por Author, pido los máximos y mínimos. 
    print(df.groupby('Author').agg({'Reviews':['min','max'], 'User Rating':'sum'})) # Agrupado por author, pedimos los mínimos y máximos de las reviews y la suma del rating del usuario. 

def convination():
    df1 = pd.DataFrame({
        'A':['A0','A1','A2','A3'],
        'B':['B0','B1','B2','B3'],
        'C':['C0','C1','C2','C3'],
        'D':['D0','D1','D2','D3'],
    })
    df2 = pd.DataFrame({
        'A':['A4','A5','A6','A7'],
        'B':['B4','B5','B6','B7'],
        'C':['C4','C5','C6','C7'],
        'D':['D4','D5','D6','D7'],
    })
    print(pd.concat([df1,df2], ignore_index=True)) # Concatenamos por fila. Con ignore_index me reorganiza los índice.
    print(pd.concat([df1,df2], axis=1)) # Concatenamos por columna.


    izq = pd.DataFrame({'key' : ['k0', 'k1', 'k2','k3'],
                        'A' : ['A0', 'A1', 'A2','A3'],
                        'B': ['B0', 'B1', 'B2','B3']})

    der = pd.DataFrame({'key' : ['k0', 'k1', 'k2','k3'],
                        'C' : ['C0', 'C1', 'C2','C3'],
                        'D': ['D0', 'D1', 'D2','D3']})
    
    
    print(izq.merge(der, on='key'))


    der = pd.DataFrame({'key_1' : ['k0', 'k1', 'k2','k3'],
                        'C' : ['C0', 'C1', 'C2','C3'],
                        'D': ['D0', 'D1', 'D2','D3']})
    
    print(izq.merge(der, left_on='key', right_on='key_1'))

    print(izq.merge(der, left_on = 'key', right_on='key_1', how='left'))

def join():
    # Join es otra herramienta para hacer exactamente lo mismo, una combinación. La diferencia es que join va a ir a los índices y no a columnas específicas.
    izq = pd.DataFrame({
                        'A': ['A0','A1','A2'],
                        'B':['B0','B1','B2']
                        },
                        index=['k0','k1','k2'])

    der =pd.DataFrame({
                        'C': ['C0','C1','C2'],
                        'D':['D0','D1','D2']
                      },
                        index=['k0','k2','k3']) 

    print(izq.join(der))
    print(izq.join(der,how='inner'))

def two_times(value):
    return value * 2

def apply():
    df = read_csv()
    print(df['User Rating'].head(2))
    print(df['User Rating'].head(2).apply(two_times)) # Le aplicó al valor de User Rating la lógica de la función two_times.

    df['User Rating2'] = df['User Rating'].head(2).apply(two_times)
    print(df)
    
    print(df['User Rating'].head(2).apply(lambda x : x * 3))

    print(df.apply(lambda x : x['User Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis=1) )
    # Le agregamos condicionales para aplicar la lógica de forma más inteligente

join() 
