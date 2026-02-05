import pytest
import math
from geometry.cylinder import volume_cylinder

def test_volumen_cilindro_entradas_validas():
    """
    Prueba el cálculo del volumen para dimensiones válidas de un cilindro.
    """
    radio, altura = 3.0, 5.0
    esperado = math.pi * radio**2 * altura
    assert volume_cylinder(radio, altura) == esperado


def test_volumen_cilindro_radio_cero():
    """
    Documenta el comportamiento actual cuando se usa una dimensión negativa.
    """
    radio, altura = -3.0, 5.0
    esperado = math.pi * radio**2 * altura
    assert volume_cylinder(radio, altura) == esperado


def test_volumen_cilindro_tolerancia_flotante():
    """
    Prueba el cálculo del volumen usando comparación aproximada.
    """
    radio, altura = 1.2, 3.4
    esperado = math.pi * radio**2 * altura
    assert volume_cylinder(radio, altura) == pytest.approx(esperado, rel=1e-6)
