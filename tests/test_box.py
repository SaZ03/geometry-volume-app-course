import pytest
from geometry.box import volume_box

def test_volumen_caja_entradas_validas():
    """
    Prueba de dimensiones válidas de una caja
    """
    ancho, alto, profundidad = 2.0, 3.0, 4.0
    esperado = 24.0
    assert volume_box(ancho, alto, profundidad) == esperado

def test_volumen_caja_dimension_negativa():
    """
    Prueba de una dimension negativa
    """
    ancho, alto, profundidad = -2.0, 3.0, 4.0
    esperado = -24.0
    assert volume_box(ancho, alto, profundidad) == esperado

def test_volumen_caja_flotante():
    """
    Prueba el cálculo cuando se usan dimensiones con punto flotante.
    """
    ancho, alto, profundidad = 1.1, 2.2, 3.3
    esperado = 7.986
    assert volume_box(ancho, alto, profundidad) == pytest.approx(esperado, rel=1e-6)
