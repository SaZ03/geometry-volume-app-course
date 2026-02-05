import pytest
import math
from geometry.cone import volume_cone

def test_volumen_cono_entradas_validas():
    """
    Prueba el cálculo del volumen para dimensiones válidas de un cono.
    """
    radio_base, altura = 3.0, 5.0
    esperado = (1 / 3) * math.pi * radio_base**2 * altura
    assert volume_cone(radio_base, altura) == esperado


def test_volumen_cono_altura_cero():
    """
    Prueba el volumen cuando la altura es cero.
    """
    radio_base, altura = -3.0, 5.0
    esperado = (1 / 3) * math.pi * radio_base**2 * altura
    assert volume_cone(radio_base, altura) == esperado


def test_volumen_cono_tolerancia_flotante():
    """
    Prueba el cálculo del volumen con comparación aproximada.
    """
    radio_base, altura = 1.5, 2.7
    esperado = (1 / 3) * math.pi * radio_base**2 * altura
    assert volume_cone(radio_base, altura) == pytest.approx(esperado, rel=1e-6)
