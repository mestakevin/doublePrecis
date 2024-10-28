import numpy as np
from scipy.optimize import rosen, minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import diff

def rosen_function():
    x = np.linspace(-2, 3, 1000)
    y = np.linspace(-2, 3, 1000)
    X, Y = np.meshgrid(x, y)
    Z = rosen(np.array([X, Y]))
    return X, Y, Z
##----------------------------------------------------------------------------##
def rosen_func(coords):
    x, y = coords
    a = 1
    b = 100
    val = ((a-x)**2) + (b*(y-(x**2))**2)
    return val
##----------------------------------------------------------------------------##
def brute_force():
	x_list = np.linspace(-2, 3, 1000)
	y_list = np.linspace(-2, 3, 1000)
	minimum = 1e10
	x = 0.0
	y = 0.0
	for i in range(len(x_list)):
		for j in range(len(y_list)):
			val = rosen([x_list[i], y_list[j]])
			if val <= minimum:
				minimum = val
				x = x_list[i]
				y = y_list[j]
	return minimum, [x, y]
	
def scipy_min():
    initial = np.array([0, 0])
    result = minimize(rosen_func, initial)
    min_val = result.fun
    [x_coord, y_coord] = result.x
    return min_val, [x_coord, y_coord]
##----------------------------------------------------------------------------##


def rosenbrock(xy):
		return rosen(xy)

##----------------------------------------------------------------------------##
def gradient_calc(x, y, delta_x, delta_y):
    der_resp_x = (rosen_func([x+delta_x, y]) - rosen_func([x-delta_x, y])) / (2*delta_x)
    der_resp_y = (rosen_func([x, y+delta_y]) - rosen_func([x, y-delta_y])) / (2*delta_y)
    return [der_resp_x, der_resp_y]
##----------------------------------------------------------------------------##
def gradient_descent(initial, alpha, delta_x, delta_y):
    grad = np.array(gradient_calc(initial[0], initial[1], delta_x, delta_y))
    new_point = [initial[0] - (alpha * grad[0]), initial[1] - (alpha * grad[1])]
    return new_point
##----------------------------------------------------------------------------##
##----------------------------------------------------------------------------##
def gradient_runner(start_coords, alpha, delta_x, delta_y, tolerance):
    point = start_coords
    point_list = []
    point_list.append(point)
    counter = 1
    while True:
        new_point = gradient_descent(point, alpha, delta_x, delta_y) 
        point_list.append(new_point)
        if ((new_point[0] - point[0])**2 + (new_point[1] - point[1])**2)**0.5 < tolerance:
            print(f"Converged after {counter} iterations.")
            break
        point = new_point
        #print(point)
        counter += 1
    return point, point_list
##----------------------------------------------------------------------------##

def newtonMethod():
	cur_pos = [0.0,0.0]
	past_pos = []
	step = 1e-3
	threshold = 1e-15
	print(step)
	print(cur_pos)
	counter = 0
	while True: 
		x_gradient = (rosen([cur_pos[0] + 1e-8, cur_pos[1]]) - rosen([cur_pos[0] - 1e-8, cur_pos[1]]))/(2 * 1e-8)
		y_gradient = (rosen([cur_pos[0], cur_pos[1] + 1e-8,]) - rosen([cur_pos[0], cur_pos[1] - 1e-8,]))/(2 * 1e-8)

		gradient_x_gradient = diff(x_gradient)
		gradient_y_gradient = diff(y_gradient) 
		
		print("x_gradient is:",x_gradient,"and y gradient is:",y_gradient)
		new_pos = [cur_pos[0] - x_gradient*step, cur_pos[1] - y_gradient*step]

		counter += 1
		if ((new_pos[0] - cur_pos[0])**2 + (new_pos[1] - cur_pos[1])**2)**0.5 < threshold:
			print("Finished after",counter,"iterations")
			break
		cur_pos = new_pos
		print(cur_pos)




def main():
	n = int(1e3)    # number of X or y
	x_list  = np.linspace(-2, 3, n)
	y_list  = np.linspace(-2, 3, n)
	X, Y    = np.meshgrid(x_list, y_list)
	delta_x = 1e-8
	delta_y = 1e-8
	alpha   = 1e-4   # step size
	start_coords = [0, 0] 
	max_iter = 1000
	tolerance = 1e-8

    # Brute_force
    #min_val, xy = brute_force(x_list, y_list)
    #print("Brute-force minimum value: ", min_val)
    #print("Coordinates: ", xy)

    # Scipy minimize
	min_val, xy = scipy_min()
	print("Scipy minimization value: ", min_val)
	print("Coordinates: ", xy)

    # Gradient descent
    #minimum_value, point_list = gradient_runner(start_coords, alpha, delta_x, delta_y, tolerance)
    #print("Gradient descent result")
    #print(point_list)
    #print("The minimum point is approximately: ", minimum_value)

    ## Path plotting for gradient descent
	corner_coords = [[-2,-2], [-2,3], [3,-2], [3,3]]
	point_list_1 = []
	point_list_2 = []
	point_list_3 = []
	point_list_4 = []
	counter = 1
	for coords in corner_coords:
		start_coords = coords
		minimum_value, point_list = gradient_runner(start_coords, alpha, delta_x, delta_y, tolerance)
		if counter == 1:
			point_list_1 = point_list
		if counter == 2:
			point_list_2 = point_list
		if counter == 3:
			point_list_3 = point_list
		if counter == 4:
			point_list_4 = point_list
		counter += 1
	x_1 = [item[0] for item in point_list_1]
	y_1 = [item[1] for item in point_list_1]
	x_2 = [item[0] for item in point_list_2]
	y_2 = [item[1] for item in point_list_2]
	x_3 = [item[0] for item in point_list_3]
	y_3 = [item[1] for item in point_list_3]
	x_4 = [item[0] for item in point_list_4]
	y_4 = [item[1] for item in point_list_4]
	plt.figure()
	plt.plot(x_1, y_1, "-.", label="[-2,-2]")
	plt.plot(x_2, y_2, "--", label="[-2,-3]")
	plt.plot(x_3, y_3, ":", label="[3,-2]")
	plt.plot(x_4, y_4, label="[3,3]")
	plt.plot(xy[0], xy[1], "*", label="minimum value")
	plt.legend()
	plt.show()

    # Create the plot
	fig = plt.figure(figsize=(8, 6))
	ax = fig.add_subplot(111, projection='3d')

    # Plot the surface
	ax.plot_surface(X, Y, rosen_func([X, Y]), cmap='viridis', edgecolor='none', alpha=0.8)

    # Customize the plot
	ax.set_title("3D Plot of the Rosenbrock Function")
	ax.set_xlabel('X-axis')
	ax.set_ylabel('Y-axis')
	ax.set_zlabel('Z-axis (Function value)')

    # Show the plot
    #plt.show()

##----------------------------------------------------------------------------##
main()