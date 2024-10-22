import numpy as np
from scipy.optimize import rosen

def rosen():
  # Create a 2D grid of points
  x = np.linspace(-2, 3, 1000)
  y = np.linspace(-2, 3, 1000)
  X, Y = np.meshgrid(x, y)
  Z = rosen(np.array[X, Y])
  return Z
