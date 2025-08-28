# Taller 1 — Computer Vision

Este repositorio contiene el desarrollo del **Taller 1 de Visión por Computadora**, que incluye la implementación de una librería en Python llamada `cvtools`.  
La librería integra funciones relacionadas con:
- **Cámara**: proyecciones y distorsiones.
- **Color**: transformaciones de espacio de color y cuantización.
- **Filtros**: detección de bordes (Sobel, Laplaciano, Canny).

Se incluyen además **demos** y **tests automáticos** para validar el correcto funcionamiento.

---

## 📂 Estructura del repositorio

```
computer-vision-taller/
├─ cvtools/
│ ├─ init.py
│ ├─ camera.py
│ ├─ color.py
│ └─ filters.py
├─ data/
│ ├─ ejemplo1.jpg
│ └─ ejemplo2.jpg
├─ tests/
│ ├─ test_camera.py
│ ├─ test_color.py
│ └─ test_filters.py
├─ main.py
├─ requirements.txt
└─ README.md
```

---

## 🐍 Recomendación de Python

El proyecto fue probado con:

- **Python 3.12.x** (recomendado).  
- Versiones muy recientes (ej. 3.14) pueden dar errores de compatibilidad en librerías como `scikit-image`.

Comprueba tus versiones en Windows:
```bash
    py -0
```

---

## 📦 Dependencias

El archivo requirements.txt contiene las librerías necesarias:
```bash
numpy>=1.26
opencv-python>=4.9
matplotlib>=3.8
scikit-image>=0.24
Pillow>=10.0
pytest>=8.0
```
---

### ⚙️ Instalación paso a paso

    1. Clonar el repositorio

        ```powershell
            git clone https://github.com/CamilaG2/computer-vision-taller1.git
            cd computer-vision-taller
        ```

    2. Crear entorno virtual

        ```powershell
            python -m venv .venv
        ```
        # Si da error por políticas de ejecución:
        # 🔧 Solución:
            1. Abre PowerShell como Administrador (clic derecho sobre PowerShell → "Ejecutar como administrador").
            2. Verifica la política actual con: 
                ```powershell
                    Get-ExecutionPolicy
                ```
            3. Si aparece 'Restricted', cambia la política a algo más permisivo, por ejemplo RemoteSigned:
                ```powershell
                    Set-ExecutionPolicy RemoteSigned
                ```
                esto te pedirá confirmación, escribe Y y enter o S y enter.
            4. Cierra PowerShell y vuelve a abrirlo en la carpeta donde se guarde el proyecto.
            5. Activa el entorno virtual: 
                ```powershell
                    venv\Scripts\Activate
                ```

    3. Actualizar pip (opcional pero recomendado)
        ```powershell
            python -m pip install --upgrade pip
        ```

    4. Instalar dependencias
        ```powershell
            pip install -r requirements.txt
        ```

---

## ▶️ Uso

    *Ejecutar la demo completa:*
    ```powershell
        python main.py
    ```

    Esto ejecutará tres demostraciones:

        - Cámara: proyección con longitud focal.

        - Color: reducción de colores y cálculo de tamaño.

        - Filtros: bordes con Sobel, Laplaciano y Canny.
    
    Tener en cuenta que para que las imágenes aparezcan hay que cerrar las otras y que algunas se demoran en verse.

    -*Ejecutar los tests*
    ```powershell
        python -m pytest
    ```
