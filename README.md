## Bienvenidos a mi proyecto Machine Learning Operations (MLOps)
Este es mí Proyecto individual donde encortraras la documentacion e instrucciones para la funcion de una api y un sistema de recomendacion de peliculas basado en puntajes.

###Funcionalidades 

- EDA_PI_MLOPS.ypynb -> archivo con el analisis exploratorio de los datos
- ETL.ipynb -> notebook con el paso a paso  del ETL
- READNE.md ->  instrucciones y documentacion del proyecto
- SISTEMA_DE_RECOMENDACION.ipynb ->archivo con la funcion de recomendacion
- main.py ->archivo de codigo para la api
- plataforma_prom.csv ->csv con el datasets que utilizamos para la API
- requirements.txt -> archivo de codigo para la api

### Funciones que ejecuta la API
🎉 Mensaje de bienvenida : [https://ejemplo-nombre-deploy-0u45.onrender.com](https://ejemplo-nombre-deploy-0u45.onrender.com)

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

⚠️ En caso que los datos de consulta sean erroneos se obtendra el siguiente mensaje: no es posible dar una respuesta, verifica los datos e intenta nuevamente

⚠️ Si ingresa una ruta no admitida recibira el siguiente mensaje: "detail":"Not Found"

✨ MUCHAS GRACIAS ✨

Agradezco el tiempo que te has tomado para testear mi api y darme un feedback :tw-1f4dd:
