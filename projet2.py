import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

data = []

with open('20villes.txt','r') as f:
    next(f)
    lines = f.readlines()
    for line in lines:
        atom = line.split(',')
        data.append(np.array(atom))

data.pop(-len(data))
print(data)

#Data generating
n = len(data)
x = np.random.rand(n,1)
y = np.random.rand(n,1)

def Probability(chemin,voisin,temperature):
    #print(chemin.getDistance(),voisin.getDistance(),temperature)
    print("->",np.exp((-1.0/temperature)*(voisin.getDistance()-chemin.getDistance())))
    return np.exp((-1.0/temperature)*(voisin.getDistance()-chemin.getDistance()))

class Point:
    def __init__(self,coord):
        self.x = coord[0]
        self.y = coord[1]
    
    def getPoint(self):
        return [self.x,self.y]
    

class Chemin:
    
    def __init__(self,n):
        self.coords = []
        for i in range(n):
            coord = [float(data[i][2]),float(data[i][1])]
            #print(coord)
            self.coords.append(Point(coord))
    
    def getDistance(self):
        
        self.distance = 0
        
        for i in range(len(self.coords)-1):
            
            x_current = self.coords[i].getPoint()[0]
            y_current = self.coords[i].getPoint()[1]
            self.distance += np.sqrt((x_current-self.coords[i+1].getPoint()[0])**2 + (y_current-self.coords[i+1].getPoint()[1])**2)
            
        x_current = self.coords[len(self.coords)-1].getPoint()[0]
        y_current = self.coords[len(self.coords)-1].getPoint()[1]
        self.distance += np.sqrt((self.coords[0].getPoint()[0] - x_current)**2 + (self.coords[0].getPoint()[1] - y_current)**2)
        
        return self.distance
    
    def getX(self):
        x_vec = []
        for i in range(len(self.coords)):
            x_vec.append(self.coords[i].getPoint()[0])
        return x_vec
    
    def getY(self):
        y_vec = []
        for i in range(len(self.coords)):
            y_vec.append(self.coords[i].getPoint()[1])
        return y_vec
    
def randomNeighbour(chemin):
    
    neighbour = Chemin(len(data))
    neighbour.coords = chemin.coords[:]
    random_point1 = random.randint(1,len(data)-2)
    random_point2 = random.randint(1,len(data)-2)
    while(random_point1 == random_point2):
        random_point2 = random.randint(1,len(data)-2)
    temp = neighbour.coords[random_point1]
    neighbour.coords[random_point1] = neighbour.coords[random_point2]
    neighbour.coords[random_point2] = temp
    return neighbour
        
chemin = Chemin(n)

#print("======================")
#neighbour = randomNeighbour(chemin)
#for i in range(len(chemin.coords)):
    #print(neighbour.coords[i].getPoint())
    
#for i in range(len(chemin.coords)):
    #print(chemin.coords[i].getPoint())

#print(chemin.getDistance(),neighbour.getDistance())

plt.plot(chemin.getX(),chemin.getY(),"-ro")
plt.legend([chemin.getDistance()])
plt.show()
T = 5000
for i in range(350000):
    voisin = randomNeighbour(chemin)
    print(chemin.getDistance(),voisin.getDistance())
    if(chemin.getDistance() > voisin.getDistance()):    
        chemin = voisin
    elif(Probability(chemin,voisin,T)>=random.uniform(0,1)):
        chemin = voisin
    T*=0.9999
    #if(i%1000==0):
	    #fig = plt.figure()
	    #plt.plot(chemin.getX(),chemin.getY(),"-ro")
	    #plt.legend([chemin.getDistance()])
	    #plt.title("Simulated annealing")
	    #buf = 'Plot2/plot'+str(i)+'.png'
	    #fig.savefig(buf)
    
chemin.coords.append(chemin.coords[0])
plt.plot(chemin.getX(),chemin.getY(),"-ro")
plt.legend([chemin.getDistance()])
plt.title("Simulated annealing")
plt.show()
