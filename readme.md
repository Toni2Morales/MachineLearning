# **Modelo de predicción de calidad del mineral de hierro en un proceso de minería**

-----

### Objetivo: Este es un proyecto en el que voy a encontrar un modelo que predica el porcentaje de sílice(impureza) que contiene un mineral después de haber sido sometido a los procesos de una planta de flotación.La pureza del mineral se puede obtener manualmente con una medida de laboratorio pero tardan al menos una hora en conseguirla, pudiendo preveer el porcentaje de pureza que tendrá el mineral al final del proceso lso ingenieros pueden tomar medidas preventivas reduciendo la impureza e impidiendo el desperdicio de porcentaje de mineral

-----

### Organización de carpetas: 

* scr/
    * data/: Contiene los archivos en formato csv usados en el proceso.
    
    * Images /: Contiene imágenes usadas en este archivo Markdown y en "proyect_resume.ipynb"

    * model/: Contiene los modelos exportados("my_model" es el modelo final elegido).

    * notebooks/: son archivos jupyter notebook usados en todo el proceso.

    * train.py/: Es el script que contiene solo los pasos para obtener el mejor modelo.


*En este repositorio se ha usado git lfs ya que los archivos csv y los modelos eran demasiado grandes*
### Fuente: [Kaggle](https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process)

------
## **Importación de los datos**




### El dataset utilizado contaba con 737453 registros y unas 24 columnas inicialmente, sin datos nulos y con los datos en tipo texto. Estas son algunas de las 23 variables que tenían los datos tras eliminar la columna de la fecha y transformar los datos a tipo numérico:

![Image](scr/Images/columnas.PNG)


### La variable a predecir es "% Silica Concentrate" y como se ve en la imagen, el porcentaje del mineral de hierro y el porcentaje de sílice antes del proceso están muy correlados y parece no tener mucha relación con la pureza que tendrán al final.

![Image](scr/Images/SilicaFeedIronFeed.png)


