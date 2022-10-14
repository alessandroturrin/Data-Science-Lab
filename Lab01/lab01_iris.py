from ast import main
from cmath import sqrt
import csv
import os 
import sys

class Iris:
    column_headers = ["Sepal length","Sepal width","Petal length","Petal width","Iris species"]
    species_list = ["All species","Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    vector = []
    avg = []
    stddev = []
    final_stddev = [0,0,0,0]
    final_avg = {}

    def __init__(self):
        with open("iris.csv") as iris_file:
            for r in csv.reader(iris_file):
                self.vector.append(r)
        self.vector.pop(len(self.vector)-1)


    def f_avg(self, flag):
        counter = 0
        self.avg = [0,0,0,0]

        for r in self.vector:
            for c in range(0,4):
                if flag=="none":
                    self.avg[c]+=float(r[c])
                else:
                    if r[4]==flag:
                        self.avg[c]+=float(r[c])
            if r[4]==flag:
                counter+=1
                
        for c in range(0,4):
            if flag=="none":
                self.avg[c] = round(self.avg[c]/len(self.vector),9)
            else:
                self.avg[c] = round(self.avg[c]/counter ,9)
        
        if flag!="none":
            self.final_avg[flag] = self.avg


    def f_stddev(self, flag):
        counter = 0
        self.stddev = [0,0,0,0]
        for r in self.vector:
            for c in range(0,4):
                if flag=="none":
                    self.stddev[c] += pow((float(r[c])-self.avg[c]),2)
                else:
                    if r[4]==flag:
                        self.stddev[c] += pow((float(r[c])-self.avg[c]),2)
            if r[4]==flag:
                counter+=1

        for c in range(0,4):       
            if flag=="none":
                self.stddev[c] = round(sqrt((1/len(self.vector))*self.stddev[c]).real,9)
            else:
                self.stddev[c] = round(sqrt((1/counter)*self.stddev[c]).real,9)
            self.final_stddev[c] += self.stddev[c]
    

    def print(self, s):
        output_file = open(self.desktop+"/iris_statistics.txt","at")
        output_str = f"--- {self.species_list[s]} statistics ---\n" + '{:25s}'.format("")

        for i in range(0,4):
            output_str += '{:25s}'.format(self.column_headers[i])
        output_str += "\n" 
        output_str += '{:25s}'.format("Average: ")
        for i in range(0,4):
            output_str += '{:25s}'.format(f"{self.avg[i]}")
        output_str += ("\n" + '{:25s}'.format("Standard deviation: "))
        for i in range(0,4):
            output_str += '{:25s}'.format(f"{self.stddev[i]}")
        output_str += "\n\n"
        print(output_str)
        output_str+="\n"
        output_file.write(output_str)
        output_file.close()
    
    
    def get_species_list(self):
        l = []
        for i in range(1,4):
            l.append(self.species_list[i])
        return l

    def f_best_measure(self):
        min_value = sys.float_info.max
        best_measure: str
        output_file = open(self.desktop+"/iris_statistics.txt","at")

        for i in range(0,len(self.final_stddev)):
            self.final_stddev[i] = self.final_stddev[i]/4
            if self.final_stddev[i]<min_value:
                min_value = self.final_stddev[i]
                best_measure = self.column_headers[i]

        output_str = "Minimum standard variation: " + f"{min(self.final_stddev)}" + " -> best measure: " + f"{best_measure}"
        print(output_str)
        output_str+="\n\n"
        output_file.write(output_str)
        output_file.close()

    
    def assign_flower(self, parameters):
        tmp_scoring = [0,0,0]
        pos = 0
        best_value = sys.float_info.max
        output_file = open(self.desktop+"/iris_statistics.txt","at")

        for i in range(0,4):
            pos=0
            for v in self.final_avg.values():
                tmp_scoring[pos]+=abs(v[i]-parameters[i])
                pos+=1

        for i in range(0,3):
            if tmp_scoring[i]<best_value:
                best_value = tmp_scoring[i]
                pos = i

        output_str = "\nInput values: " + f"{parameters}" + " -> " + f"{self.species_list[pos+1]}: {self.final_avg[self.species_list[pos+1]]}"
        print(output_str)
        output_str+="\n"
        output_file.write(output_str)
        output_file.close()
            

if __name__=="__main__":
    iris = Iris()
    #2.1.2
    iris.f_avg("none")
    iris.f_stddev("none")
    iris.print(0)
    #2.1.3
    species_list = iris.get_species_list()
    for i in range(0,len(species_list)):
        iris.f_avg(species_list[i])
        iris.f_stddev(species_list[i])
        iris.print(i+1)
    #2.1.4
    iris.f_best_measure()
    #2.1.5
    test = [[5.2,3.1,4.0,1.2],[4.9,2.5,5.6,2.0],[5.4,3.2,1.9,0.4]]
    for i in test:
        iris.assign_flower(i)

    

    
    
        
    



