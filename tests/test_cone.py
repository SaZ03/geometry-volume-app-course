import pytest
import math
from geometry.cone import volume_cone

def test_volumen_cono_entradas_validas():
    """
    Prueba el cálculo del volumen para dimensiones válidas de un cono.
    """
    radio_base, altura = 5.0, 2.0
    esperado = 52.3598775598
    assert volume_cone(radio_base, altura) == pytest.approx(esperado, rel=1e-6)


def test_volumen_cono_altura_cero():
    """
    Prueba el volumen cuando la altura es cero.
    """
    radio_base, altura = 7.0, 0.0
    esperado = 0
    assert volume_cone(radio_base, altura) == esperado


def test_volumen_dimension_negativa():
    """
    Prueba el volumen cuando la base es negativa.
    """
    radio_base, altura = -7.0, 4.0
    esperado = 205.250720035
    assert volume_cone(radio_base, altura) == pytest.approx(esperado, rel=1e-6)

