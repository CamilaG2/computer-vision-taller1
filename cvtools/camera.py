# camera.py
import numpy as np

def distorsion_radial(puntos, k1=0, k2=0):
    x, y = puntos[:,0], puntos[:,1]
    r2 = x**2 + y**2
    factor = 1 + k1*r2 + k2*(r2**2)
    x_dist = x * factor
    y_dist = y * factor
    return np.column_stack((x_dist, y_dist))


def distorsion_completa(puntos, k1=0, k2=0, k3=0, p1=0, p2=0):
    x, y = puntos[:,0], puntos[:,1]
    r2 = x**2 + y**2
    
    # Radial
    radial = 1 + k1*r2 + k2*r2**2 + k3*r2**3
    x_radial = x * radial
    y_radial = y * radial
    
    # Tangencial
    x_tang = 2*p1*x*y + p2*(r2 + 2*x**2)
    y_tang = p1*(r2 + 2*y**2) + 2*p2*x*y
    
    # Distorsión total
    x_dist = x_radial + x_tang
    y_dist = y_radial + y_tang
    
    return np.column_stack((x_dist, y_dist))


def longitud_focal(puntos, f):
    x, y, z = puntos[:,0], puntos[:,1], puntos[:,2]
    z = np.where(z == 0, 1e-6, z) 
    x_proj = (f * x) / z
    y_proj = (f * y) / z
    return np.column_stack((x_proj, y_proj))
