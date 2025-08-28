# filters.py
import cv2
import numpy as np

def convolucion(img, kernel):
    return cv2.filter2D(img, -1, kernel)


def sobel_x(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    return cv2.convertScaleAbs(sobelx)  # convierte a uint8 para visualizar


def sobel_y(img):
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    return cv2.convertScaleAbs(sobely)


def canny(img, t1=100, t2=200):
    return cv2.Canny(img, t1, t2)


def laplaciano(img):
    lap = cv2.Laplacian(img, cv2.CV_64F)
    return cv2.convertScaleAbs(lap)  # convierte a uint8 para visualizar
