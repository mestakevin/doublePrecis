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
	
def minimization():
	# Calculating minimum value by scipy minimization
	x = np.linspace(-2, 3, 1000)
	y = np.linspace(-2, 3, 1000)
	xy = [x, y]
		
	initial_guess = np.array([0, 0])  # Starting point for optimization
	result = minimize(rosenbrock, initial_guess)
	print("SciPy minimization value: ", result.fun)
	print("SciPy minimization coordinate: ", result.x)


def rosenbrock(xy):
		return rosen(xy)

def gradientMethod():
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

		print("x_gradient is:",x_gradient,"and y gradient is:",y_gradient)
		new_pos = [cur_pos[0] - x_gradient*step, cur_pos[1] - y_gradient*step]

		counter += 1
		if ((new_pos[0] - cur_pos[0])**2 + (new_pos[1] - cur_pos[1])**2)**0.5 < threshold:
			print("Finished after",counter,"iterations")
			break
		cur_pos = new_pos
		print(cur_pos)
         
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
	#minimum, [x, y] = brute_force()
	#print("Brute-force minimum value: ", minimum)
	#print("Brute-force minimum coordinate: ", [x, y])
	#minimization()
	X, Y, Z = rosen_function()

	gradientMethod()
	
	# 3D plot
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

	ax.set_title("Rosenbrock Function")
	ax.set_xlabel("X-axis")
	ax.set_ylabel("Y-axis")
	ax.set_zlabel("Z-axis (Function Value)")

	#plt.show()
	
main()
