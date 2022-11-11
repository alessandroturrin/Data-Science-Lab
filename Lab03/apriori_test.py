from itertools import compress, product
import collections

def f_combinations(items):
    return (set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)))

def apriori(data):
    combinations = []
    for row in data:
        combinations.extend(f_combinations(row))
    combinations = list(filter((set()).__ne__, combinations))
    occurrences = { ' '.join(item):combinations.count(item) for item in combinations }
    final_occurrences = {k:v for k,v in occurrences.items() if v>1 }
    return final_occurrences
    


data = []
maxlen = 0
with open('test_file.txt') as mc_file:
    raw_data = mc_file.readlines()

sup_str = raw_data[0].split(' ')
for s in sup_str:
    l = s.split(',')
    data.append(sorted(l))

final_dict = apriori(data)
print(final_dict)



