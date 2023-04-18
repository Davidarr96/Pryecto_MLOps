## Bienvenidos a mi proyecto Machine Learning Operations (MLOps)
![](https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png)

Mi nombre es David Arrieta, y en esta ocación, la empresa Henry nos contrata como científicos de datos para realizar una API y un modelo de Machine Learning  para consultas y recomendaciones de las seguiente plataformas : Netflix, Amazon, Disney Plus y Hulu.

La empresa nos provee los siguientes [Datasets](https://drive.google.com/drive/folders/1b49OVFJpjPPA1noRBBi1hSmMThXmNzxn)

A continuación, indicaremos lo logrado por nuestro equipo:

### Funcionalidades 

- [EDA_PI_MLOPS.ipynb](https://github.com/Davidarr96/Pryecto_MLOps/blob/main/EDA_PI_MLOPS.ipynb) -> archivo con el analisis exploratorio de los datos
- [ETL.ipynb](https://github.com/Davidarr96/Pryecto_MLOps/blob/main/ETL.ipynb) -> notebook con el paso a paso  del ETL
- [README.md](https://github.com/Davidarr96/Pryecto_MLOps/blob/main/README.md) ->  instrucciones y documentacion del proyecto
- [SISTEMA_DE_RECOMENDACION.ipynb](https://github.com/Davidarr96/Pryecto_MLOps/blob/main/SISTEMA_DE_RECOMENDACION.ipynb) ->archivo con la funcion de recomendacion
- [main.py](https://github.com/Davidarr96/Pryecto_MLOps/blob/main/main.py) ->archivo de codigo para la api
- [plataforma_prom.csv](https://github.com/Davidarr96/Pryecto_MLOps/blob/main/plataformas_prom.csv) ->csv con el datasets que utilizamos para la API
- [requirements.txt](https://github.com/Davidarr96/Pryecto_MLOps/blob/main/requirements.txt) -> archivo txt para el deployado de nuestra api

### Funciones que ejecuta la API
🎉 Mensaje de bienvenida : [Hola](https://ejemplo-nombre-deploy-0u45.onrender.com)

✔️ Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.

🚀 [LINK](https://ejemplo-nombre-deploy-0u45.onrender.com/docs#/default/get_max_duration_get_max_duration__year___platform___duration_type__get)


✔️ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

🚀 [LINK](https://ejemplo-nombre-deploy-0u45.onrender.com/docs#/default/get_score_count_get_score_count__platform___scored___year__get)


✔️ Cantidad de películas por plataforma con filtro de PLATAFORMA.

🚀 [LINK](https://ejemplo-nombre-deploy-0u45.onrender.com/docs#/default/get_count_platform_get_count_platform__platform__get)


✔️ Actor que más se repite según plataforma y año.

🚀 [LINK](https://ejemplo-nombre-deploy-0u45.onrender.com/docs#/default/get_actor_get_actor__platform___year__get)


✔️ La cantidad de contenidos/productos que se publicó por país y año.

🚀 [LINK](https://ejemplo-nombre-deploy-0u45.onrender.com/docs#/default/prod_per_county_prod_per_county__tipo___pais___anio__get)


✔️ La cantidad total de contenidos/productos  según el rating de audiencia dado.

 🚀 [LINK](https://ejemplo-nombre-deploy-0u45.onrender.com/docs#/default/get_contents_get_contents__rating__get)
 

#### ADVERTENCIA 

⚠️Las plataformas admitidas son: ['amazon','disney','hulu','netflix']

⚠️ En caso que los datos de consulta sean erroneos se obtendra el siguiente mensaje: Not Found o internal error-.

⚠️ El formato de tiempo es en min; en platadormas se admite la inicial de cada una (d=disney, a=amazon, n=netflix, h=hulu)

✨ MUCHAS GRACIAS ✨

Agradezco el tiempo que te has tomado para testear mi api y darme un feedback 💪
