#Ellipse circumference 
import numpy as np
from matplotlib import pyplot as plt
from math import pi
import random
import statistics

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
    if (x ** 2 / a1 ** 2 + y ** 2 / b1 ** 2 <= 1) and (x ** 2 / a2 ** 2 + y ** 2 / b2 ** 2 >= 1):
        return True
    else:
        return False
    
##----------------------------------------------------##
def main():
    u = 0.0    #x-position of the center
    v = 0.0    #y-position of the center
    a = 5.0    #radius on the x-axis
    b = 2.0    #radius on the y-axis
  
    #scale factor for the inner ellipse (very smart)
    dk = 0.97
    a2 = a*dk 
    b2 = b*dk
    thickness = (a - a2 + b - b2) / 2
  
    t = np.linspace(0, 2*pi, 100)
    
    #Rectangle bounds
    x_min = u - a
    x_max = u + a
    y_min = v - b
    y_max = v + b
    area_rect = (2 * a) * (2 * b)

    #Random number generator in a rectangle
    points_in_bound = 0
    points_total = 5000

    accept_x = []
    accept_y = []
    reject_x = []
    reject_y = []

    for i in range (points_total):
        rand_num_x = random.uniform(x_min, x_max)
        rand_num_y = random.uniform(y_min, y_max)
        if check_ellipse(rand_num_x, rand_num_y, a, b, a2, b2):
            points_in_bound += 1
            accept_x.append(rand_num_x)
            accept_y.append(rand_num_y)
        else:
            reject_x.append(rand_num_x)
            reject_y.append(rand_num_y)
    result_ratio = points_in_bound / points_total
    area_ellipse = area_rect * result_ratio
    circ_ellipse = area_ellipse / thickness

    plt.plot(u + (a*np.cos(t)), v + b*np.sin(t) , label= f"Original ellipse" )
    plt.plot(u + (a2*np.cos(t)), v + (b2*np.sin(t)) , label= f"Inner ellipse" )
    plt.plot(accept_x, accept_y,
            color = '#66ff00', # bright green
            marker = "d",
            linestyle = "None",
            markersize = 3,
            label = f"Accepted Points: {points_in_bound}, ellipse circumference: {circ_ellipse:.2f}")
    
    plt.plot(reject_x, reject_y,
            color = '#ffb7c5', # cherry blossom pink
            marker = "d",
            linestyle = "None",
            markersize = 1,
            label = f"Rejected Points: {points_total - points_in_bound}")
    

    plt.grid(color='lightgray',linestyle='--')
    # plt.show()
    plt.legend()

    plot_destination = "figures/ellipse.png"
    plt.savefig(plot_destination, dpi=500)
    plt.clf()


    ##------------------------statistical error----------------------------##
    npoints_list = np.arange(100, 3001, 100)
    standev_list = []

    for points in npoints_list:
        circ_list = []
        for trial in range (1000): # for each dart sample size, repeat 1000 times
            points_in_bound = 0
            for i in range (points):
                rand_num_x = random.uniform(x_min, x_max)
                rand_num_y = random.uniform(y_min, y_max)
                if check_ellipse(rand_num_x, rand_num_y, a, b, a2, b2):
                    points_in_bound += 1
            result_ratio = points_in_bound / points
            area_ellipse = area_rect * result_ratio
            circ_ellipse = area_ellipse / thickness
            circ_list.append(circ_ellipse)

        standev_list.append(statistics.stdev(circ_list))

        print(f"Number of Darts: {points}")
        # print(f"Lowest: {min(circ_list):.2f}")
        # print(f"Highest: {max(circ_list):.2f}")
        # print(f"Mean: {statistics.mean(circ_list):.2f}")
        print(f"Standard Deviation: {statistics.stdev(circ_list):.2f}")
        print(f"")

    plt.plot(npoints_list, standev_list,
            color = '#7fffd4', # aquamarine
            marker = "d",
            linestyle = "None",
            markersize = 10,
            label = f"Data")
    plt.title(f"Statistical Error vs Sample Points, Ellipse Circumference")
    plt.xlabel(f"Number of Dart Sample for each Simulation")
    plt.ylabel(f"Standard Deviation of 1000 Circumference Simulations")
    plot_destination = "figures/ellipse_sim.png"
    plt.savefig(plot_destination, dpi=500)
##----------------------------------------------------##

if __name__ == "__main__":
    main()
