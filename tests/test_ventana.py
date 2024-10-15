import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.ventana import Ventana

def test_valores_entidades():
    estilo = "X"
    ancho = 20
    alto = 80
    acabado = "Pulido"
    tipo_vidrio = "Azul"
    esmerilado = False

    ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado)

    assert ventana.estilo == estilo
    assert ventana.ancho == ancho
    assert ventana.alto == alto
    assert ventana.acabado == acabado
    assert ventana.tipo_vidrio == tipo_vidrio
    assert ventana.esmerilado == esmerilado

def test_valor_aluminio():
    estilo = "O"
    ancho = 12
    alto = 15
    acabado = "Pulido"
    tipo_vidrio = "Transparente"
    esmerilado = False

    ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado)

    aluminio_esperado = 15210

    assert ventana.calcular_valor_aluminio() == aluminio_esperado

def test_costo_vidrio():
    estilo = "O"
    ancho = 12
    alto = 15
    acabado = "Pulido"
    tipo_vidrio = "Transparente"
    esmerilado = False

    ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado)

    costo_esperado = 891

    assert ventana.calcular_valor_vidrio() == costo_esperado