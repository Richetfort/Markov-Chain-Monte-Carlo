import numpy as np
import random

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
            coord = [random.uniform(0,10),random.uniform(0,10)]
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

def factoriel(n):
    facto = 1
    for i in range(1,n+1):
        facto *= i
    return facto    

def permutations(configurations,vector,size,storage_index,added):
    temp = np.array([None]*len(vector))
    for i in range(1,size):
        for j in range(0,len(vector)-size):
            temp[j] = vector[j]
        k=0
        for j in range(len(vector)-size,len(temp)):
            temp[j] = vector[len(vector)-size:][(i+k)%size]
            k+=1
        configurations[storage_index+i-1+added] = temp

def configurations_listing(v,n,n_facto):
    configurations = np.array([[None]*n]*n_facto)
    configurations[0] = v
    storage_index = 1

    size = n
    storage_index = 1
    while(size > 1):
        added = 0
        for i in range(0,storage_index):
            permutations(configurations,configurations[i],size,storage_index,added)
            added += (size-1)
        storage_index += added
        size -= 1
    return configurations
initial_route = Chemin(4)
n = len(initial_route.coords)
n_facto = factoriel(n)

configurations = configurations_listing(initial_route.coords,n,n_facto)
print(configurations)
#P = np.zeros((n,n))
