from array import array
from cProfile import label
from cmath import log
import csv
from lib2to3.pgen2 import token
from symbol import term
import numpy as np
import os 
import matplotlib.pyplot as plt
import string
from collections import Counter, ChainMap

from itertools import islice
os.system('clear')

def tokenize(docs):
    term_frequency = []
    for doc in docs:
        for punct in string.punctuation:
            doc = doc.replace(punct, " ")
        split_doc = [ token.lower() for token in doc.split(" ") if token ]
        term_frequency.append(split_doc)
    return term_frequency

def term_frequency_f():
    for review in reviews:
        term_frequency.append(Counter(review))
    
def inverse_document_frequency_f():
    N = len(reviews)
    document_frequency = dict()
    
    for k,v in [(key,d[key]) for d in term_frequency for key in d]:
        if k not in document_frequency: 
            document_frequency[k]=1
        else: 
            document_frequency[k] += 1

    inv_document_frequency = document_frequency.copy()

    for k,v in inv_document_frequency.items():
        inv_document_frequency[k] = log(N/v).real
    return inv_document_frequency

def tf_idf_f():
    for i in range(0,len(tf_idf)):
        for k,v in tf_idf[i].items():
            tf_idf[i][k] = v*inv_document_frequency[k]


term_frequency = list()
document_frequency = dict()
inv_document_frequency = dict()
tf_idf = list()

with open("aclimdb_reviews_train.csv", "r") as acrt_file:
    data = list()
    labels = list()
    for r in csv.reader(acrt_file):
        data.append(r[0])
        labels.append(r[1])
    data.pop(0)
    labels.pop(0)

reviews = tokenize(data)
term_frequency_f()
inv_document_frequency = inverse_document_frequency_f()
tf_idf = term_frequency[:]
tf_idf_f()
print(tf_idf[0],"\n\n",term_frequency[0])