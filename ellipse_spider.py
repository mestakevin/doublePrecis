#Ellipse circumference 
<<<<<<< HEAD

def check_ellipse(x, y, a1, b1, a2, b2):
    """
    This method checks if the given point falls in between the ellipses.
        'x' -- given point x coordinate
        'y' -- given point y coordinate
        'a1' -- semi maJor axis of larger ellipse
        'b1' -- semi miNor axis of larger ellipse
        'a2' -- semi maJor axis of smaller ellipse
        'b1' -- semi miNor axis of smaller ellipse
    """
    if (x ** 2 / a1 ** 2 + y ** 2 / b1 ** 2 < 1) and (x ** 2 / a2 ** 2 + y ** 2 / b2 ** 2 > 1):
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()
    
    

=======
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
>>>>>>> fcdac1d5fe56992b4046999f8a456572baec9de5
