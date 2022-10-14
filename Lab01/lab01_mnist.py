from cmath import sqrt
import csv
import os
from turtle import distance 
import sys

class Mnist:
    vector = []
    values = []
    hashmap = {}
    distances = {}

    def __init__(self) -> None:
        with open("mnist.csv") as mnist_file:
            for r in csv.reader(mnist_file):
                self.vector.append(r)
        mnist_file.close()
        self.mapper_init()

        for i in self.vector:
            self.values.append(int(i[0]))
            i.pop(0)


    def mapper_init(self):
        for i in range(0,64):
            self.hashmap[i] = " "
        for i in range(64,128):
            self.hashmap[i] = "."
        for i in range(128,192):
            self.hashmap[i] = "*"
        for i in range(192,256):
            self.hashmap[i] = "#"


    def print(self, img):
        counter = 0
        for i in self.vector[img]:
            if counter%28==0:
                print(f"\n{self.hashmap[int(i)]}", end="")
            else:
                print(self.hashmap[int(i)],end="")
            counter+=1
        print("")
    

    def euclidean_distanc_calc(self,d1,d2):
        vct = []
        distance = 0
        for i,j in zip(self.vector[d1],self.vector[d2]):
            distance += (int(i)-int(j))**2
        distance = sqrt(distance).real
        print(distance)

        if d1<d2:
            self.distances[f"{d1}_{d2}"] = vct 
        else:
            self.distances[f"{d2}_{d1}"] = vct 


    def euclidean_distance(self, vector):
        for i in range(0, len(vector)-1):
            for j in range(i+1, len(vector)):
                self.euclidean_distanc_calc(vector[i-1],vector[j-1])

    
    def check(self):
        Z = [0]*784
        O = [0]*784
        maxval = sys.float_info.min
        pos = -1

        for iterator in range(0,len(self.values)):
            if self.values[iterator]==1:
                for i in range(0,len(self.vector[iterator])):
                    if int(self.vector[iterator][i])<128:
                        Z[i]+=1
            elif self.values[iterator]==0:
                for i in range(0,len(self.vector[iterator])):
                    if int(self.vector[iterator][i])<128:
                        O[i]+=1
            
        for i in range(0,784):
            if abs(Z[i]-O[i])>maxval:
                maxval = abs(Z[i]-O[i])
                pos = i
        
        print(f"Max distance: {maxval} at position {pos}")


if __name__=='__main__':        
    os.system('clear')

    mnist = Mnist()
    mnist.euclidean_distance([25,29,31,34])
    mnist.check()



