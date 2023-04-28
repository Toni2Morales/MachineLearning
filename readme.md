# **Modelo de predicción de calidad del mineral de hierro en un proceso de minería**

-----
*En este repositorio se ha usado git lfs para las carpetas de data y model ya que los archivos csv y los modelos eran demasiado grandes, para usar los modelos y archivos csv se tendrán que descargar desde github*
### Objetivo: Este es un proyecto en el que voy a encontrar un modelo que predica el porcentaje de sílice(impureza) que contiene un mineral después de haber sido sometido a los procesos de una planta de flotación.La pureza del mineral se puede obtener manualmente con una medida de laboratorio pero tardan al menos una hora en conseguirla, pudiendo preveer el porcentaje de pureza que tendrá el mineral al final del proceso lso ingenieros pueden tomar medidas preventivas reduciendo la impureza e impidiendo el desperdicio de porcentaje de mineral



-----

### Organización de carpetas: 

* scr/
    * data/: Contiene los archivos en formato csv usados en el proceso.
    
    * Images /: Contiene imágenes usadas en este archivo Markdown y en "proyect_resume.ipynb"

    * model/: Contiene los modelos exportados("my_model" es el modelo final elegido).

    * notebooks/: son archivos jupyter notebook usados en todo el proceso.

    * train.py/: Es el script que contiene solo los pasos para obtener el mejor modelo.

------

### Fuente: [Kaggle](https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process)

------

### En este proyecto de pueden apreciar conocimientos en:

* Análisis de datos
* Aprendizaje supervisado
* Modelos ensamblados
* Modelos de regresión
* Interpretación del modelo
* RandomSearch
* Regularización

------
## **Importación de los datos**




#### El dataset utilizado contaba con 737453 registros y unas 24 columnas inicialmente, sin datos nulos y con los datos en tipo texto. Estas son algunas de las 23 variables que tenían los datos tras eliminar la columna de la fecha y transformar los datos a tipo numérico:


% Iron Feed|	% Silica Feed	|Starch Flow|	Amina Flow	|Ore Pulp Flow	|Ore Pulp pH|	Ore Pulp Density|	Flotation Column 01 Air Flow|	Flotation Column 04 Air Flow	|Flotation Column 05 Air Flow	|Flotation Column 06 Air Flow|	Flotation Column 01 Level	|Flotation Column 02 Level|	Flotation Column 03 Level	|Flotation Column 04 Level|	Flotation Column 05 Level|	Flotation Column 06 Level|	Flotation Column 07 Level|	% Silica Concentrate
---|---|---|----|-----|-----|-----|-----|-----|----|----|-----|-----|-----|------|-----|-----|------|----
0|	55.2|	16.98|	3019.53|	557.434|	395.713|	10.0664|	1.74|	249.214|	295.096|	306.4|	250.225|	457.396|	432.962|	424.954|	443.558|	502.255|	446.370|	523.344|	1.31
1|	55.2|	16.98|	3024.41|	563.965|	397.383|	10.0672|	1.74|	249.719|	295.096|	306.4|	250.137|	451.891|	429.560|	432.939|	448.086|	496.363|	445.922|	498.075|	1.31
2|	55.2|	16.98|	3043.46|	568.054|	399.668|	10.0680|	1.74|	249.741|	295.096|	306.4|	251.345|	451.240|	468.927|	434.610|	449.688|	484.411|	447.826|	458.567|	1.31
3|	55.2|	16.98|	3047.36|	568.665|	397.939|	10.0689|	1.74|	249.917|	295.096|	306.4|	250.422|	452.441|	458.165|	442.865|	446.210|	471.411|	437.690|	427.669|	1.31
4|	55.2|	16.98|	3033.69|	558.167|	400.254|	10.0697|	1.74|	250.203|	295.096|	306.4|	249.983|	452.441|	452.900|	450.523|	453.670|	462.598|	443.682|	425.679|	1.31
5|	55.2|	16.98|	3079.10|	564.697|	396.533|	10.0705|	1.74|	250.730|	295.096|	306.4|	250.356|	444.384|	443.269|	460.449|	439.920|	451.588|	433.539|	425.458|	1.31
6|	55.2|	16.98|	3127.79|	566.467|	392.900|	10.0713|	1.74|	250.313|	295.096|	306.4|	250.950|	446.185|	444.571|	452.306|	431.328|	443.548|	444.575|	431.251|	1.31

#### La variable a predecir es "% Silica Concentrate" y como se ve en la imagen, el porcentaje del mineral de hierro y el porcentaje de sílice antes del proceso están muy correlados y parece no tener mucha relación con la pureza que tendrán al final.

![Image](scr/Images/SilicaFeedIronFeed.png)

![Image](scr/Images/SilicaConcentrateSilicaFeed.PNG)

![Image](scr/Images/IronConcentrateIronFeed.PNG)

![Image](scr/Images/SilicaConcentrateIronConcentrate.PNG)

## **Análisis de los datos**
#### Aquí podemos ver como nuestros datos de la variable objetivo se concentran en valores que están entre 3 y 1.5. Podemos vre que tenemos unos cuantos valores atípicos por encima de 5 pero no se alejan demasiado

![Image](scr/Images/BoxPlot.PNG)

#### Este es un gráfico de densidad con el que podemos apreciar de otra manera la distribución de los datos de la variable que queremos predecir. Como vemos, los datos se concentran en los mismos valores anteriormente dichos.

![Image](scr/Images/GraficaDeDensidad.PNG)

#### Podemos ver que hay ciertas correlaciones que son de variables que son partes del proceso muy parecidas así que esas las ignoraremos. También vemos que no hay ninguna variable que tenga una correlación fuerte con la concentración de sílice aunque la que tiene mayor relación es la variable del flujo de amina(Amina Flow)

![Image](scr/Images/Heatmap.PNG)

#### Podemos ver una correlación de 0.66 "Amina Flow" y "Ore Pulp Density" así que vamos a ver cómo se correlan.

![Image](scr/Images/AminaOrePulpDensity.PNG)

#### Se puede observar que hay una correlación tal vez logaritmica entre estas dos variables y como vimos antes, la variable Amina Flow es la que más correlación tiene con la variable objetivo.

## *Correlación con la variable objetivo*

#### Ahora vamos a realizar un análisis la variable más importante con respecto a la concentración de sílice final.

#### En la imagen vemos cierto direccionamiento de los valores pero nada realmente muy notable(recordemos que tiene una correlación de solo 0.66).

![Image](scr/Images/AminaFlowSilicaConcentrate.PNG)

## **Modelo Final**

> #### Probamos
   * Regresión Lineal
   
      ![Imagen1](scr/Images/RegresionLineal.PNG)
      * Ridge
      
         ![Imagen1](scr/Images/RegresionLineal.PNG)
      * Lasso
      
         ![Imagen1](scr/Images/RegresionLineal.PNG)
      * ElasticNet

         ![Imagen1](scr/Images/RegresionLineal.PNG)
   * Arbol de decisiones

      ![Imagen1](scr/Images/ArbolDeDecisiones.PNG)
   * RandomForest

      ![Imagen1](scr/Images/RandomForest.PNG)
------
#### También probamos

   * ExtraTreeRegressor

   * SVC

   * KNN

   * Modelos aplicando Grid Search y Cross Validation

#### Al final el mejor modelo es un Random Forest que fue encontrado con un RandomSearch.

![IMAGEN](scr/Images/MejorModelo.PNG)

#### La primera métrica indica el error absoluto medio que indica que de media las predicciones se desvían un 0,08 del resultado real mientras que con la segunda métrica podemos ver que normalmente no vamos a tener ningún error grande. La tercera métrica es el error porcentual absoluto medio indicando un error de un 0.04% de error y el último error indica la raíz del error cuatrático medio con un valor de 0,01.

#### El mejor modelo que hemos obtenido ha sido usando el algoritmo de random forest(un modelo ensamblado que usa varios modelos de arboles de decision). Vamos a visualizar el comienzo de uno de estos arboles de decisiones.

![Image](scr/Images/RandomForestOneScheme.PNG)

#### Los arboles de decision se basan en muchas elecciones en base a diferentes criterios que llevarán a crear diferentes ramas dependiendo de todas las elecciones que hayan para que al final se tome una decisión final con respecto al valor de la variable a predecir. Como se ve en la imagen, se va evaluando si un valor de una variable es mayor o menor a otro y dependiendo de esta evaluacion se va a una rama u a otra sucesivamente hasta llegar a un nodo final que nos indicará el resultado.

## Feature Importance

#### Por último vamos a ver las variables con mayor implicación a la hora de que el modelo realice sus predicciones.

#### Puedes ver que las variables con mayor correlación fueron % Iron Feed y % Silica Feed y luego serían Ore Pulp pH, la cual no me esperaba que tuviera tanta importancia, y Amina Flow

![Image](scr/Images/FeatureImportances.PNG)

![Image](scr/Images//FeatureImportances2.PNG)
