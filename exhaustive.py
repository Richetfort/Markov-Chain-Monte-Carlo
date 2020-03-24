import numpy as np
import matplotlib.pyplot as plt
import random
import time

start_time = time.time()

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
    
def print_configurations(configurations,n,n_facto):
    for i in range(0,n_facto):
        print("======== ",i+1," ========")
        for j in range(0,n):
            print(configurations[i].coords[j].getPoint())
        print("=====================")

def factoriel(n):
    facto = 1
    for i in range(1,n+1):
        facto *= i
    return facto    

def permutations(configurations,route,size,storage_index,added):
    temp = [None]*len(route.coords)
    for i in range(1,size):
        for j in range(0,len(route.coords)-size):
            temp[j] = route.coords[j]
        k=0
        for j in range(len(route.coords)-size,len(temp)):
            temp[j] = route.coords[len(route.coords)-size:][(i+k)%size]
            k+=1
        configurations[storage_index+i-1+added].coords = temp[:]

def configurations_listing(initial_route,n,n_facto):
    configurations = []
    for i in range(n_facto):
        configurations.append(Chemin(n))
    print(configurations)
    configurations[0] = initial_route
    storage_index = 1
    
    size = n-1
    storage_index = 1
    while(size > 1):
        added = 0
        for i in range(0,storage_index):
            permutations(configurations,configurations[i],size,storage_index,added)
            added += (size-1)
        storage_index += added
        size -= 1
    return configurations

def best_route(configurations,n,n_facto):
    best_configuration = configurations[0]
    for i in range(1,n_facto):
        if(best_configuration.getDistance()>configurations[i].getDistance()):
            best_configuration = configurations[i]
    return best_configuration

initial_route = Chemin(9)
n = len(initial_route.coords)
n_facto = factoriel(n-1)

configurations = configurations_listing(initial_route,n,n_facto)
print_configurations(configurations,n,n_facto)
best_configuration = best_route(configurations,n,n_facto)

print("--- %s seconds ---" % (time.time() - start_time))
initial_route.coords.append(initial_route.coords[0])
best_configuration.coords.append(best_configuration.coords[0])

plt.plot(initial_route.getX(),initial_route.getY(),'-ro')
plt.plot(initial_route.getX()[0],initial_route.getY()[0],'bo')
plt.legend([initial_route.getDistance(),"Starting Point"])
plt.show()

plt.plot(best_configuration.getX(),best_configuration.getY(),'-go')
plt.plot(initial_route.getX()[0],initial_route.getY()[0],'bo')
plt.legend([best_configuration.getDistance(),"Starting Point"])
plt.show()
#P = np.zeros((n,n))
