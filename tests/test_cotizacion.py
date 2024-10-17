import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.cotizacion import Cotizacion
from app.ventana import Ventana

def test_descuento_empresa():
    cliente = "Juan Diaz"
    ventana = Ventana("O", 12.0, 15.0, "Pulido", "Transparente", False)
    cant_ventanas = 102

    cotizacion = Cotizacion(cliente, ventana, cant_ventanas)

    descuento_esperado = 3060703.8

    assert cotizacion.calcular_total() == descuento_esperado