#Ellipse circumference 
import numpy as np
from matplotlib import pyplot as plt
from math import pi
import random


##----------------------------------------------------##
def main():
    u = 0.0    #x-position of the center
    v = 0.0    #y-position of the center
    a = 5.0    #radius on the x-axis
    b = 2.0    #radius on the y-axis
  
    #scale factor for the inner ellipse
    dk = 0.97
    a2 = a*dk 
    b2 = b*dk
  
    t = np.linspace(0, 2*pi, 100)
    plt.plot(u + (a*np.cos(t)), v + b*np.sin(t) , label= "Original ellipse" )
    plt.plot(u + (a2*np.cos(t)), v + (b2*np.sin(t)) , label= "Inner ellipse" )
    plt.grid(color='lightgray',linestyle='--')
    plt.show()
    
    #Rectangle bounds
    x_min = u - a
    x_max = u + a
    y_min = v - b
    y_max = v + b 
    #Random number generator in a rectangle
    rand_num_x = random.uniform(x_min, x_max)
    rand_num_y = random.uniform(y_min, y_max)
    

##----------------------------------------------------##
main()
