import pytest
import math
from geometry.sphere import volume_sphere

def test_volumen_esfera_entrada_valida():
    """
    Prueba el cálculo para dimensiones válidas.
    """
    radio = 3.0
    esperado = 113.097335529
    assert volume_sphere(radio) == pytest.approx(esperado, rel=1e-6)


def test_volumen_esfera_radio_negativo():
    """
    Prueba el uso de una dimensión negativa.
    """
    with pytest.raises(ValueError):
        volume_sphere(-2.0)

        # sphere.py ya verifica si hay valores iguales a 0 o menores


def test_volumen_esfera_flotante():
    """
    Prueba el uso de dimensiones con punto flotante.
    """
    radio = 1.7
    esperado = 20.5795262761
    assert volume_sphere(radio) == pytest.approx(esperado, rel=1e-6)
