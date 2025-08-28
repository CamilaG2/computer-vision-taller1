# tests/test_camera.py
import numpy as np
from cvtools import camera

def test_distorsion_radial_sin_cambios():
    puntos = np.array([[0.5, 0.5], [-0.5, -0.5]])
    result = camera.distorsion_radial(puntos, k1=0, k2=0)
    # Sin distorsión, debe ser igual
    assert np.allclose(result, puntos)

def test_distorsion_radial_con_cambio():
    puntos = np.array([[0.5, 0.5]])
    result = camera.distorsion_radial(puntos, k1=0.1, k2=0.01)
    # Con distorsión, debe cambiar
    assert not np.allclose(result, puntos)

def test_distorsion_completa_sin_cambios():
    puntos = np.array([[0.2, -0.3], [0.0, 0.0]])
    result = camera.distorsion_completa(puntos, k1=0, k2=0, k3=0, p1=0, p2=0)
    # Sin distorsión, debe ser igual
    assert np.allclose(result, puntos)

def test_distorsion_completa_tangencial():
    puntos = np.array([[0.5, 0.5]])
    result = camera.distorsion_completa(puntos, p1=0.1, p2=-0.1)
    # El resultado debe seguir siendo 2D y sin NaN
    assert result.shape == (1,2)
    assert not np.isnan(result).any()

def test_longitud_focal_basico():
    puntos = np.array([[1.0, 2.0, 5.0], [2.0, 4.0, 10.0]])
    result = camera.longitud_focal(puntos, f=10)
    # Debe proyectar a 2D
    assert result.shape == (2,2)

def test_longitud_focal_z_cero():
    puntos = np.array([[1.0, 1.0, 0.0]])  # z=0
    result = camera.longitud_focal(puntos, f=10)
    # Debe devolver números válidos
    assert not np.isnan(result).any()
    assert not np.isinf(result).any()
