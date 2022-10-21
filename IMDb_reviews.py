from array import array
import csv
import numpy as np
import os 
import matplotlib.pyplot as plt 

#0-Date [discrete]
#1-AvgTemp [continuous]
#2-AvgTempErr [continuous]
#3-City [nominal]
#4-Country [nominal]
#5-Lat [continuous]
#6-Long [continuous]

os.system('clear')

def topNhc(city, N):
    tmp = np.array(glt[city])
    tmp.sort()

    topNH = tmp[len(tmp)-N-1:len(tmp)-1]
    topNC = tmp[0:N-1]

    print(f"Top {N} hottest temperatures")
    print(list(reversed(topNH)))
    print(f"\nTop {N} coldest temperatures")
    print(topNC)

def converter(city):
    glt[city] = list(map(lambda x: (float(x)-32)/1.8,glt[city]))

with open("GLT_filtered.csv", "r") as glt_file:
    glt = dict()

    for r in csv.reader(glt_file):
        glt.setdefault(r[3], []).append(r)

for k, v in glt.items():
    tmp = list()
    
    [tmp.append(i[1]) for i in v]

    for i in range(0,len(tmp)):
        if tmp[i]=='':
            j = i
            while j<len(tmp)-1 and tmp[j]=='':
                j += 1
            if tmp[j]=='':
                val = 0
            else:
                val = float(tmp[j])

            if i==0:
                tmp[i] = val/2
            elif i<len(tmp)-1:
                tmp[i] = (float(tmp[i-1])+val)/2
            else:
                tmp[i] = float(tmp[i-1])/2
        tmp[i] = '{:.1f}'.format(float(tmp[i]))
    glt[k] = np.array(tmp)

topNhc("Abidjan", 10)
print(len(glt["Rome"]))
plt.xlabel("Temperatures")
plt.ylabel("Frequencies")
plt.hist(glt["Rome"], edgecolor="black")
plt.hist(glt["Bangkok"], edgecolor="black")
plt.show()

#5*
converter("Bangkok")
plt.hist(glt["Rome"], edgecolor="black")
plt.hist(glt["Bangkok"], edgecolor="black")
plt.show()




