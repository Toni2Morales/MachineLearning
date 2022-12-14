import pandas as pd
import pickle
from datetime import datetime
import os
os.chdir("scr")
def train(model):
    # Leyendo el modelo que se quiere entrenar
    with open(model, 'rb') as f:
        MODELO = pickle.load(f)
    train = pd.read_csv("data/Train.csv", index_col="Unnamed: 0")
    xtrain = train.drop(columns = "% Silica Concentrate")
    ytrain = train["% Silica Concentrate"]
    # Entrenando el modelo
    MODELO.fit(xtrain, ytrain)
    # Exportando el modelo
    with open("model/model_" + datetime.now().strftime('%Y%m%d%H%M%S'), 'wb') as f:
        pickle.dump(model, f)
#Entrenamos el modelo deseado usando su ruta
train("my_model")