import cv2
import numpy as np
import matplotlib.pyplot as plt
from cvtools import camera, color, filters

def demo_camera():
    print("\n--- DEMO CAMERA ---")

    # Grid de puntos 2D
    x = np.linspace(-1, 1, 10)
    y = np.linspace(-1, 1, 10)
    xv, yv = np.meshgrid(x, y)
    puntos_2d = np.column_stack((xv.ravel(), yv.ravel()))

    # Distorsión radial
    dist_radial = camera.distorsion_radial(puntos_2d, k1=0.3, k2=0.05)

    # Distorsión completa
    dist_completa = camera.distorsion_completa(puntos_2d, k1=0.1, k2=0.05, p1=0.1, p2=-0.1)

    # Visualización
    plt.figure(figsize=(12,4))
    plt.subplot(1,2,1)
    plt.scatter(puntos_2d[:,0], puntos_2d[:,1], c="b", label="Original", s=10)
    plt.scatter(dist_radial[:,0], dist_radial[:,1], c="r", label="Radial", s=10)
    plt.legend(); plt.title("Distorsión radial")

    plt.subplot(1,2,2)
    plt.scatter(puntos_2d[:,0], puntos_2d[:,1], c="b", label="Original", s=10)
    plt.scatter(dist_completa[:,0], dist_completa[:,1], c="g", label="Completa", s=10)
    plt.legend(); plt.title("Distorsión completa")
    plt.show()

    # Proyección con longitud focal
    puntos_3d = np.array([[1,2,5],[2,4,10],[3,1,8]], dtype=float)
    proy = camera.longitud_focal(puntos_3d, f=10)
    print("Proyección con longitud focal:", proy)


def demo_color():
    print("\n--- DEMO COLOR ---")
    img = cv2.imread("data/ejemplo1.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    hsv = color.rgb_to_hsv(img_rgb)
    lab = color.rgb_to_lab(img_rgb)
    yuv = color.rgb_to_yuv(img_rgb)

    # Mostrar espacios de color
    plt.figure(figsize=(12,4))
    plt.subplot(1,3,1); plt.imshow(hsv); plt.title("HSV"); plt.axis("off")
    plt.subplot(1,3,2); plt.imshow(lab); plt.title("LAB"); plt.axis("off")
    plt.subplot(1,3,3); plt.imshow(yuv); plt.title("YUV"); plt.axis("off")
    plt.show()

    # Histograma
    color.histograma_color(img_rgb)

    # Cuantización
    cuant = color.cuantizacion(img_rgb, 8)
    plt.imshow(cuant); plt.title("Cuantización a 8 colores"); plt.axis("off")
    plt.show()

    # Reducción de peso
    _, size_kb = color.reducir_peso(img_rgb, 16)
    print(f"Tamaño de imagen tras reducción de colores: {size_kb:.2f} KB")


def demo_filters():
    print("\n--- DEMO FILTERS ---")

    img_gray = cv2.imread("data/ejemplo2.jpg", cv2.IMREAD_GRAYSCALE)

    sobelx = filters.sobel_x(img_gray)
    sobely = filters.sobel_y(img_gray)
    canny_edges = filters.canny(img_gray, 100, 200)
    lap = filters.laplaciano(img_gray)

    plt.figure(figsize=(12,6))
    plt.subplot(2,2,1); plt.imshow(sobelx, cmap="gray"); plt.title("Sobel X"); plt.axis("off")
    plt.subplot(2,2,2); plt.imshow(sobely, cmap="gray"); plt.title("Sobel Y"); plt.axis("off")
    plt.subplot(2,2,3); plt.imshow(canny_edges, cmap="gray"); plt.title("Canny"); plt.axis("off")
    plt.subplot(2,2,4); plt.imshow(lap, cmap="gray"); plt.title("Laplaciano"); plt.axis("off")
    plt.show()


if __name__ == "__main__":
    demo_camera()
    demo_color()
    demo_filters()
    print("\nDemostración completa ✅")
