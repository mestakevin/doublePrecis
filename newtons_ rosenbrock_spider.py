import numpy as np
import matplotlib.pyplot as plt

# rosenbrock function
def rosenbrock(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

# finding the gradient of rosenbrock function to use in newton's metho
def gradient(x):
    df_dx0 = -2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0]**2)
    df_dx1 = 200 * (x[1] - x[0]**2)
    return np.array([df_dx0, df_dx1])

# hessian to use in newton's method
def hessian(x):
    d2f_dx0x0 = 2 - 400 * (x[1] - 3 * x[0]**2)
    d2f_dx0x1 = -400 * x[0]
    d2f_dx1x0 = -400 * x[0]
    d2f_dx1x1 = 200
    return np.array([[d2f_dx0x0, d2f_dx0x1],
                     [d2f_dx1x0, d2f_dx1x1]])

# Newton's method
def newton_method(start, tol=1e-6, max_iter=1000):
    x = np.array(start, dtype=float)
    path = [x.copy()]
    
    for _ in range(max_iter):
        grad = gradient(x)
        hess = hessian(x)
        
        # solve H * delta = -grad
        delta = np.linalg.solve(hess, -grad)
        x = x + delta
        
        path.append(x.copy())
        
        if np.linalg.norm(grad) < tol:
            break
    
    return x, path

# list of initial points
starting_points = [(3, 3), (-2, 2), (2, 1)]
all_paths = []

# find the minimum for each starting point and collect paths
for start_point in starting_points:
    min_point, path = newton_method(start_point)
    all_paths.append((min_point, path))

# plot
plt.figure(figsize=(10, 6))

for min_point, path in all_paths:
    path = np.array(path)
    plt.plot(path[:, 0], path[:, 1], marker='*', markersize=5, label=f'Path from {path[0]} to {min_point}')

plt.scatter(*zip(*[min_point for min_point, _ in all_paths]), color='red', s=100, label='Minimum points', edgecolor='black')
plt.title("Paths of Newton's Method on Rosenbrock Function")
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.grid()
plt.show()
