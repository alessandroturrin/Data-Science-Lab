from math import sqrt
import numpy as np
from itertools import islice
from collections import Counter

class KNearestNeighbors:
    def __init__(self, k, distance_metric="euclidean"):
        self.k = k
        self.distance_metric = distance_metric
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    #1.1.6
    def predict(self, X):
        shortest_dist_indexes = list()
        predictions = []
        for item in X:
            distances = {}
            for i in range(len(self.X_train)):
                distances[i] = self.euclidean_distance(self.X_train[i], item)
            distances = dict(sorted(distances.items(), key=lambda x:x[1]))
            shortest_dist_indexes.append(list(islice(distances.keys(), self.k)))
        
        for l in shortest_dist_indexes:
            predictions.append(self.assign_label(l)[0][0])
        return np.array(predictions)

    #1.1.5
    def euclidean_distance(self, p, q):
        return ((p-q)**2).sum()**.5
    
    def cosine_distance(p, q):
        return 1-abs((p*q).sum()/((p**2).sum()*(q**2).sum()))

    def manhattan_distance(p, q):
        return abs(p-q).sum()

    def assign_label(self, shortest_dist_indexes):
        votes = list()
        for i in shortest_dist_indexes:
            votes.append(self.y_train[i])
        return Counter(votes).most_common()

    def accuracy_score(self, y_pred, y_test):
        correct = (y_pred==y_test).sum()
        accuracy = correct/len(y_pred)
        print(f"{correct} correct out of {len(y_pred)} -> {round(accuracy*100, 2)}% accuracy")
