from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score,confusion_matrix, precision_score, recall_score, f1_score
from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt

import numpy as np

def f1(X):
    print(f'Dataset contains {len(X)} records')
    print('X -> missing values') if np.isnan(X).any() else print('X -> no missing values')
    print(f'Elements per classi: {np.shape(X)[0]}')

def f2(X,y):
    clf = DecisionTreeClassifier()
    clf.fit(X,y)
    return clf

def f3(clf):
    plot_tree(clf)
    plt.show()

def f4(clf, X, y_true):
    y_pred = clf.predict(X)
    acc_scr = accuracy_score(y_true, y_pred)
    print(f'accuracy score: {acc_scr}')

def f5(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
    return X_train, X_test, y_train, y_test

def f6(X_train, X_test, y_train, y_test):
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc_scr = accuracy_score(y_test, y_pred)
    print(confusion_matrix(y_test, y_pred))
    print(precision_score(y_test, y_pred, average=None))
    print(recall_score(y_test, y_pred, average=None))
    print(f1_score(y_test, y_pred, average=None))

def f7():
    params = {
    "max_depth": [None, 2, 3, 4, 5],
    "min_impurity_decrease": [0, .01, .03, .07, .09, .11]
    }
    accuracies = []
    for config in ParameterGrid(params):
        clf = DecisionTreeClassifier(**config)
        clf.fit(X_train, y_train)
        accuracies.append(accuracy_score(y_test, clf.predict(X_test)))
    max(accuracies)

def f8():
    params = {
    "max_depth": [None, 2, 3, 4, 5],
    "min_impurity_decrease": [0, .01, .03, .07, .09, .11]
    }
    X_train_valid, X_test, y_train_valid, y_test = train_test_split(X, y, stratify=y)
    kf = KFold(5)

    accuracies = []
    for config in ParameterGrid(params):
        clf_accuracies = []
        counts = []
        for train_indices, valid_indices in kf.split(X_train_valid):
            X_train = X_train_valid[train_indices]
            y_train = y_train_valid[train_indices]
            X_valid = X_train_valid[valid_indices]
            y_valid = y_train_valid[valid_indices]
    
            counts.append(len(train_indices)) 

            clf = DecisionTreeClassifier(**config)
            clf.fit(X_train, y_train)
            acc = accuracy_score(y_valid, clf.predict(X_valid))
            clf_accuracies.append(acc)
        accuracies.append(np.average(clf_accuracies, weights=counts))

if __name__=='__main__':
    dataset = load_wine()
    X = dataset["data"]
    y = dataset["target"]
    feature_names = dataset["feature_names"]
    
    #f1(X)
    clf = f2(X,y)
    #f3(clf)
    f4(clf, X, y)
    X_train, X_test, y_train, y_test = f5(X,y)
    f6(X_train, X_test, y_train, y_test)
    f7()
    f8()