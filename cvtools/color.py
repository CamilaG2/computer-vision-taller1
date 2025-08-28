# color.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb_to_hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

def rgb_to_lab(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2LAB)

def rgb_to_yuv(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2YUV)

def histograma_color(img):
    colores = ('b','g','r')
    for i,col in enumerate(colores):
        hist = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(hist, color=col)
    plt.title("Histograma de colores")
    plt.show()

def cuantizacion(img, k):
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    _, labels, centers = cv2.kmeans(Z, k, None,
                                    (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
                                    10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    result = centers[labels.flatten()]
    return result.reshape(img.shape)

def reducir_peso(img, k):
    cuant = cuantizacion(img, k)
    _, buffer = cv2.imencode(".jpg", cuant)
    size_kb = len(buffer) / 1024
    return cuant, size_kb
