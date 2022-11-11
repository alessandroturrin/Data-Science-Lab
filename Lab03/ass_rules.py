import csv 
from mlxtend.frequent_patterns import fpgrowth, association_rules
from timeit import timeit
import pandas as pd

def f_presence_matrix(invoices, all_items):
    position_dictionary = { k:v for v,k in enumerate(all_items)}
    presence_matrix = []
    n_items = len(all_items)
    for invoice in invoices.values():
        row = [False] * n_items
        for item in invoice:
            row[position_dictionary[item]] = True
        presence_matrix.append(row)
    return presence_matrix
    

#2.1.1
data = []
with open('online_retail.csv') as or_file:
    for row in csv.reader(or_file):
        if not row[0].startswith('C'):
            data.append(row)
header = data.pop(0)

#2.1.2
invoices = {}
for row in data:
    if row[0] not in invoices:
        invoices[row[0]] = set()
    invoices[row[0]].add(row[2])

#2.1.3
all_items_set = set()
for items in invoices.values():
    all_items_set.update(items)
all_items = sorted(list(all_items_set))
presence_matrix = f_presence_matrix(invoices, all_items)
df = pd.DataFrame(data=presence_matrix, columns=all_items)

#2.1.4/5
freq_itemsets = fpgrowth(df, 0.02) 
print((len(freq_itemsets))) #303
print(freq_itemsets[freq_itemsets["itemsets"].map(len)>1])

#2.1.6
M = df.values
support_2656 = len(M[M[:, 2656]]==True)/len(M)
support_1599 = len(M[M[:, 1599]]==True)/len(M)
support_tot = len(M[(M[:, 2656] == True) & (M[:, 1599] == True)])/len(M)
print(f"Confidence 2656 => 1599: {support_tot / support_2656}")
print(f"Confidence 1599 => 2656: {support_tot / support_1599}")

#2.1.7
freq_itemsets = fpgrowth(df, 0.01) 
association_rules(freq_itemsets, 'confidence', 0.85)