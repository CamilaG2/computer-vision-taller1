# tests/test_color.py
import cv2
import os
from cvtools import color

# Rutas de imágenes de prueba
DATA_DIR = "data"
IMG1 = os.path.join(DATA_DIR, "ejemplo1.jpg")
IMG2 = os.path.join(DATA_DIR, "ejemplo2.jpg")

def test_rgb_to_hsv():
    img = cv2.imread(IMG1)
    hsv = color.rgb_to_hsv(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    assert hsv.shape == img.shape

def test_rgb_to_lab():
    img = cv2.imread(IMG1)
    lab = color.rgb_to_lab(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    assert lab.shape == img.shape

def test_rgb_to_yuv():
    img = cv2.imread(IMG2)
    yuv = color.rgb_to_yuv(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    assert yuv.shape == img.shape

def test_cuantizacion():
    img = cv2.imread(IMG2)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = color.cuantizacion(img_rgb, 8)
    assert result.shape == img_rgb.shape

def test_reducir_peso():
    img = cv2.imread(IMG1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result, size_kb = color.reducir_peso(img_rgb, 16)
    assert result.shape == img_rgb.shape
    assert size_kb > 0
