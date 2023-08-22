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

manejo_nulos()