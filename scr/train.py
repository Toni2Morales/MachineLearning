import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from datetime import datetime
Data = pd.read_csv("data/Dataset_definitivo.csv", index_col="Unnamed: 0")
# Decllaración de X, Y y el dataset de train y test
X = Data.iloc[:, :-1]
Y = Data.iloc[:, -1]
xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size = 0.2, random_state = 3)
# Entrenando el primer modelo
modelo3 = RandomForestRegressor(n_estimators=5)
modelo3.fit(xtrain, ytrain)
# Probando varios hiperparámetros con RandomSearch y cross validation
RS = RandomizedSearchCV(estimator = modelo3, param_distributions = {"n_estimators": [17, 18, 19, 20, 21, 22],"max_depth": range(79, 82), "min_samples_split": [3,4,5,6]}, verbose=3, n_iter = 20, cv = 2)
RS.fit(xtrain, ytrain)
modelo_final = RS.best_estimator_
# Exportando el modelo
with open("model/model_" + datetime.now().strftime('%Y%m%d%H%M%S'), 'wb') as f:
    pickle.dump(modelo_final, f)