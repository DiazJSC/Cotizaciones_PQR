import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.cliente import Cliente
from app.ventana import Ventana

def test_valores_entidades():
    nombre = "Juan Diaz"
    empresa = "kreinps"

    clientes = Cliente(nombre, empresa)

    assert clientes.nombre_cliente == nombre
    assert clientes.nombre_empresa == empresa