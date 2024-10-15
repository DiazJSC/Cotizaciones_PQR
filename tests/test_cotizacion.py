import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.cotizacion import Cotizacion
from app.ventana import Ventana

def test_descuento_empresa():
    cliente = "Juan Diaz"
    ventana = Ventana("O", 12.0, 15.0, "Pulido", "Transparente", "N")
    cant_ventanas = 102

    cotizacion = Cotizacion(cliente, ventana, cant_ventanas)

    descuento_esperado = 3060703.8

    #assert cotizacion.calcular_total() == descuento_esperado
    print(f"Costo aluminio: {ventana.calcular_valor_aluminio()}")
    print(f"Costo vidrio: {ventana.calcular_valor_vidrio()}")
    print(f"Costo esquinas: {ventana.calcular_valor_esquinas()}")
    print(f"Costo accesorios: {ventana.calcular_valor_accesorios()}")
    assert abs(cotizacion.calcular_total() - descuento_esperado) < 0.01