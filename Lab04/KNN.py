import pandas as pd
import numpy as np
import random as rd
import os
from KNearestNeighborsM import KNearestNeighbors

os.system('clear')

#1.1.1
df = pd.read_csv('iris.csv', header=None)
k = 10
#1.1.2
X = df.values[:, :4].astype(float)
y = df.values[:, 4]
indexes_hm = list(range(0,len(df)))
mask = np.array([False]*int(len(df)*0.2)+[True]*int(len(df)*0.8))
np.random.shuffle(mask)
X_test = X[~mask]
y_test = y[~mask]

#1.1.3
X_train = X[mask]
y_train = y[mask]

#1.1.4
knn = KNearestNeighbors(k)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

for i in range(len(X_test)):
    print(f"i={i}\tpredicted specie: {y_pred[i]}\texcpected specie: {y_test[i]}")

knn.accuracy_score(y_pred,y_test)

