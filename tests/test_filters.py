# tests/test_filters.py
import cv2
import os
import numpy as np
from cvtools import filters

# Directorio de datos y rutas de imágenes
DATA_DIR = "data"
IMG1 = os.path.join(DATA_DIR, "ejemplo1.jpg")
IMG2 = os.path.join(DATA_DIR, "ejemplo2.jpg")

def test_convolucion_identity():
    img = cv2.imread(IMG1, cv2.IMREAD_GRAYSCALE)
    kernel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]], dtype=np.float32)
    result = filters.convolucion(img, kernel_identity)
    assert result.shape == img.shape

def test_sobel_x():
    img = cv2.imread(IMG2, cv2.IMREAD_GRAYSCALE)
    result = filters.sobel_x(img)
    assert result.shape == img.shape
    assert result.dtype == np.uint8 

def test_sobel_y():
    img = cv2.imread(IMG2, cv2.IMREAD_GRAYSCALE)
    result = filters.sobel_y(img)
    assert result.shape == img.shape
    assert result.dtype == np.uint8

def test_canny():
    img = cv2.imread(IMG1, cv2.IMREAD_GRAYSCALE)
    result = filters.canny(img, 100, 200)
    assert result.shape == img.shape
    unique_vals = np.unique(result)
    assert all(val in [0, 255] for val in unique_vals)

def test_laplaciano():
    img = cv2.imread(IMG1, cv2.IMREAD_GRAYSCALE)
    result = filters.laplaciano(img)
    assert result.shape == img.shape
    assert result.dtype == np.uint8
