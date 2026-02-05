import pytest
import math
from geometry.cylinder import volume_cylinder

def test_volumen_cilindro_entradas_validas():
    """
    Prueba el cálculo del volumen para dimensiones válidas de un cilindro.
    """
    radio, altura = 3.0, 5.0
    esperado = 141.371669412
    assert volume_cylinder(radio, altura) == pytest.approx(esperado, rel=1e-6)


def test_volumen_cilindro_negativo():
    """
    Prueba cuando se usa una dimensión negativa.
    """
    radio, altura = 3.0, -5.0
    esperado = -141.371669412
    assert volume_cylinder(radio, altura) == pytest.approx(esperado, rel=1e-6)


def test_volumen_cilindro_flotante():
    """
    Prueba el cálculo cuando se usan dimensiones con punto flotante.
    """
    radio, altura = 1.2, 3.4
    esperado = 15.381237632
    assert volume_cylinder(radio, altura) == pytest.approx(esperado, rel=1e-6)
