import pytest
from geometry.box import volume_box

def test_volumen_caja_entradas_validas():
    """
    Prueba el cálculo del volumen para dimensiones válidas de una caja.
    """
    ancho, alto, profundidad = 2.0, 3.0, 4.0
    esperado = 24.0
    assert volume_box(ancho, alto, profundidad) == esperado

def test_volumen_caja_dimension_negativa():
    """
    Documenta el comportamiento actual cuando se usa una dimensión negativa.
    """
    ancho, alto, profundidad = -2.0, 3.0, 4.0
    esperado = -24.0
    assert volume_box(ancho, alto, profundidad) == esperado

def test_volumen_caja_tolerancia_flotante():
    """
    Prueba el cálculo del volumen usando comparación aproximada.
    """
    ancho, alto, profundidad = 1.1, 2.2, 3.3
    esperado = ancho * alto * profundidad
    assert volume_box(ancho, alto, profundidad) == pytest.approx(esperado, rel=1e-6)
