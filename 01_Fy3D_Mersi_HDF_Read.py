import numpy as np
from scipy.interpolate import RegularGridInterpolator

def F(u, v):
    return u * np.cos(u * v) + v * np.sin(u * v)

fit_points = [np.linspace(0, 3, 8), np.linspace(0, 3, 8)]
print(*fit_points)

values = F(*np.meshgrid(*fit_points, indexing='ij'))

ut, vt = np.meshgrid(np.linspace(0, 3, 80), np.linspace(0, 3, 80), indexing='ij')

true_values = F(ut, vt)

test_points = np.array([ut.ravel(), vt.ravel()]).T

interp = RegularGridInterpolator(fit_points, values)

im = interp(test_points, method="linear").reshape(80, 80)