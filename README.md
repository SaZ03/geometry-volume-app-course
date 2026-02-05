# geometry-volume-app-course
Simula una calculadora simple de volúmenes de geometría

# Descripción del proyecto
Este proyecto proporciona una colección simple y escalable de funciones en Python para calcular el volumen de formas 3D tales como cajas, conos, cilindros y esferas.

# Explicación de la estructura del proyecto
Los contenidos principales del proyecto incluyen dos carpetas, un archivo main.py y un README.md.

La carpeta 'geometry' contiene archivos Python separados para cada forma compatible. Cada archivo contiene la definición de la función utilizada para calcular el volumen de la forma.

Actualmente, los archivos son:
- box.py
- cone.py
- cylinder.py
- sphere.py

La carpeta 'tests' contiene archivos Python separados para cada forma compatible. Cada archivo contiene 3 pruebas unitarias que se realizan en cada función de volumen, verificando el comportamiento de la función.

Actualmente, los archivos son:
- test_box.py
- test_cone.py
- test_cylinder.py
- test_sphere.py

La carpeta raíz también contiene este README.md, así como el archivo main.py que debe ejecutarse para usar la calculadora. Este archivo es un menú, desde el cual puedes acceder a las diferentes funciones disponibles.

Finalmente, la carpeta raíz contiene requirements.txt, un archivo que incluye todos los paquetes de terceros necesarios para ejecutar este proyecto.

# Cómo ejecutar main.py

1. Instala los requisitos previos con `pip install -r requirements.txt`, si no se ha hecho anteriormente.
2. Abre una terminal en el directorio de la carpeta raíz.
3. Ejecuta `python main.py`

# Cómo ejecutar las pruebas
1. Instala los requisitos previos con `pip install -r requirements.txt`, si no se ha hecho anteriormente.
2. Abre una terminal en el directorio de la carpeta raíz.
3. Ejecuta `pytest`

# Dependencias
- Python
- pytest>=7.0
