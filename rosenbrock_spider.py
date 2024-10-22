import numpy as np
from scipy.optimize import rosen, minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
	def rosenbrock(xy):
		return rosen(xy)
		
	initial_guess = np.array([0, 0])  # Starting point for optimization
	result = minimize(rosenbrock, initial_guess)
	print("SciPy minimization value: ", result.fun)
	print("SciPy minimization coordinate: ", result.x)

def gradientMethod():
    
	#x_list = np.random.uniform(-2,3,n)
	#y_list = np.random.uniform(-2,3,n)
    inital_pos = (0,0)
    while True:
        past_positions = []
        step_size = 0.005
        #x_grad = 

def main():
	minimum, [x, y] = brute_force()
	print("Brute-force minimum value: ", minimum)
	print("Brute-force minimum coordinate: ", [x, y])
	minimization()
	X, Y, Z = rosen_function()
	
	# 3D plot
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

	ax.set_title("Rosenbrock Function")
	ax.set_xlabel("X-axis")
	ax.set_ylabel("Y-axis")
	ax.set_zlabel("Z-axis (Function Value)")

	plt.show()
	
main()
