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


def test_volumen_esfera_entrada_cero():
    """
    Prueba el uso de una dimensión cero.
    """
    radio = 0.0
    esperado = 0.0
    assert volume_sphere(radio) == esperado

def test_volumen_esfera_flotante():
    """
    Prueba el uso de dimensiones con punto flotante.
    """
    radio = 1.7
    esperado = 20.5795262761
    assert volume_sphere(radio) == pytest.approx(esperado, rel=1e-6)
