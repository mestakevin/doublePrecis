import numpy as np
from scipy.optimize import rosen
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rosen_function():
    x = np.linspace(-2, 3, 1000)
    y = np.linspace(-2, 3, 1000)
    X, Y = np.meshgrid(x, y)
    Z = rosen(np.array([X, Y]))
    return X, Y, Z

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
