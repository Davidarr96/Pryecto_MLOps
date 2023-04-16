#Paso 1: Importamos las librerias FastAPI, pandas y numpy
import pandas as pd, numpy as np
from fastapi import FastAPI
#Paso 2: importamos los datos a utilizar
data_plataformas = pd.read_csv('plataforma_prom.csv')
#Paso 3: crea un "instance" de FastAPI
app = FastAPI()

async def root():
    return{"message": "Hello my friends"}

#Consultas
'''
Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
    La función debe llamarse get_max_duration(year, platform, duration_type) '''
    
@app.get("/get_max_duration")
async def get_max_duration(year: int, platform: str, duration_type: str):
    
 

    # 1. Filtro por año
    filtro_anio = data_plataformas.loc[ data_plataformas['release_year'] == year ]

    # 2. Filtro por plataforma
    # a: amazon, d: disney, h: hulu, n: netflix
    filtro_plataforma = filtro_anio.loc[ filtro_anio['Id'].str[0:1] == platform ]

    # 3. Filtro por tipo de duracion
    filtro_tipo_duracion = filtro_plataforma.loc[ filtro_plataforma['duration_type'] == duration_type ]

    # 4. Filtro de mayor duracion
    max_duracion = filtro_tipo_duracion.loc[ filtro_tipo_duracion['duration_int'] == filtro_tipo_duracion['duration_int'].max() ]
    
    movie_max_duracion = max_duracion['title']

    return movie_max_duracion

'''
Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
    La función debe llamarse get_score_count(platform, scored, year) '''

@app.get("/get_score_count")
async def get_score_count(platform: str, scored: float, year: int):
    
    # 1. Filtro por año
    filtro_anio = data_plataformas.loc[ data_plataformas['release_year'] == year ]

    # 2. Filtro por score
    filtro_score = filtro_anio.loc[ filtro_anio['score'] > scored ]

    # 3. Agrupar por plataforma y contar peliculas
        #creamos la columna 'platform' para poder agrupar más adelante
    filtro_score['plataforma'] = filtro_score['Id'].str[0]

        # Agrupamos las películas por plataforma y contamos el número de películas en cada plataforma
    peliculas_x_plataformas = filtro_score.groupby('plataforma').size().reset_index(name='count')

    # 4. Filtrar por plataforma
    plataforma_y_peliculas = peliculas_x_plataformas.loc[ peliculas_x_plataformas['plataforma'] == platform ]

    resultado = plataforma_y_peliculas [ plataforma_y_peliculas['plataforma'] == platform[0] ]
    resultado = resultado['count']
        
    return 'La plataforma', platform, 'tiene', int(resultado), 'peliculas, publicadas en el año', year, 'con score mayor a', scored



'''
Cantidad de películas por plataforma con filtro de PLATAFORMA. 
    La función debe llamarse get_count_platform(platform) '''

@app.get("/get_count_platform")
async def get_count_platform(platform: str):

    import pandas as pd
    data_plataformas = pd.read_csv('plataformas_prom.csv', sep=',')

    # 1. Creamos nueva columna con letra de plataforma
    data_plataformas['plataforma'] = data_plataformas['Id'].str[0]

    # 2. Agrupamos las películas por plataforma y contamos el número de películas en cada plataforma
    peliculas_x_plataformas = data_plataformas.groupby('plataforma').size().reset_index(name='count')

    # 3. Filtrar por plataforma
    plataforma_y_peliculas = peliculas_x_plataformas.loc[ peliculas_x_plataformas['plataforma'] == platform ]

    resultado = plataforma_y_peliculas [ plataforma_y_peliculas['plataforma'] == platform[0] ]
    resultado = resultado['count']
  
    return 'La plataforma', platform, 'tiene', int(resultado), 'peliculas publicadas.'



'''
Actor que más se repite según plataforma y año.
    La función debe llamarse get_actor(platform, year) '''

@app.get("/get_actor")
async def get_actor(platform: str, year: int):

    import pandas as pd
    data_plataformas = pd.read_csv('plataformas_prom.csv', sep=',')
    
    # 1. Filtramos los registros por año dado por parametro
    filtro_anio = data_plataformas.loc[ data_plataformas['release_year'] == year ]

    # 2. Filtramos los registros por plataforma dado por parametro
    filtro_plataforma_anio = filtro_anio.loc[ filtro_anio['Id'].str[0] == platform ]

    # 3. Filtramos los cast sin dato, para que no aparezcan en el conteo de actores
    cast_con_datos = filtro_plataforma_anio [ filtro_plataforma_anio['cast'] != 'sin dato' ]

    # 4. Dividir los nombres de los actores en una lista y contar las ocurrencias de cada uno
    actor_counts = cast_con_datos['cast'].str.split(',').explode().str.strip().value_counts()

    # 5. Devolver el nombre del actor más frecuente
    most_frequent_actor = actor_counts.index[0]
        
    return most_frequent_actor
