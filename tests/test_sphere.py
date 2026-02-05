import pytest
import math
from geometry.sphere import volume_sphere

def test_volumen_esfera_entrada_valida():
    """
    Prueba el cálculo del volumen para dimensiones válidas.
    """
    radio = 3.0
    esperado = (4 / 3) * math.pi * radio**3
    assert volume_sphere(radio) == esperado


def test_volumen_esfera_radio_negativo():
    """
    Documenta el comportamiento actual cuando se usa una dimensión negativa.
    """
    with pytest.raises(ValueError):
        volume_sphere(-2.0)

        # sphere.py ya verifica explícitamente valores iguales a 0 o menores


def test_volumen_esfera_tolerancia_flotante():
    """
    Prueba el cálculo del volumen usando comparación aproximada.
    """
    radio = 1.7
    esperado = (4 / 3) * math.pi * radio**3
    assert volume_sphere(radio) == pytest.approx(esperado, rel=1e-6)
