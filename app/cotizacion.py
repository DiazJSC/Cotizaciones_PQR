import json
import os
from rich.table import Table
from rich.console import Console
current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, "datos.json")

console = Console()

with open(json_path, "r") as file:
    config = json.load(file)

class Cotizacion:
    def __init__(self, cliente, ventana, cant_ventanas):
        self.cliente = cliente
        self.ventana = ventana
        self.cantidad_ventanas = cant_ventanas
        self.descuento = config["descuento"]

    def calcular_total(self):
        costo_aluminio = self.ventana.calcular_valor_aluminio()
        costo_vidrio = self.ventana.calcular_valor_vidrio()
        costo_esquinas = self.ventana.calcular_valor_esquinas()
        costo_acce = self.ventana.calcular_valor_accesorios()

        total = (costo_aluminio + costo_vidrio + costo_esquinas + costo_acce) * self.cantidad_ventanas

        if self.cantidad_ventanas > 100:
            total_descuento = total * self.descuento
            total -= total_descuento

        return total
    
    def mostrar_cotizacion(self):
        nombre_cliente = self.cliente.nombre_cliente
        nombre_empresa = self.cliente.nombre_empresa
        estilo = self.ventana.estilo
        ancho = self.ventana.ancho
        alto = self.ventana.alto
        acabado = self.ventana.acabado
        vidrio = self.ventana.tipo_vidrio
        esmerilado = self.ventana.esmerilado

        table = Table(title="Cotización")

        table.add_column("Descripción", style="cyan", justify="center")
        table.add_column("Detalle", style="magenta", justify="center")

        table.add_row("Nombre del cotizante", nombre_cliente)
        table.add_row("Empresa destinataria", nombre_empresa)
        table.add_row("Estilo de ventana", estilo)
        table.add_row("Dimensiones (cm)", f"{ancho} x {alto}")
        table.add_row("Acabado", acabado)
        table.add_row("Tipo de vidrio", vidrio)
        table.add_row("Esmerilado", "Sí" if esmerilado else "No")
        table.add_row("Cantidad de ventanas", str(self.cantidad_ventanas))

        return table
    
    @classmethod
    def mostrar_tarifas(cls, opcion):
        cls.vlr_pulido = str(config["costo_aluminio"]["Pulido"])
        cls.vlr_brillante = str(config["costo_aluminio"]["Lacado Brillante"])
        cls.vlr_mate = str(config["costo_aluminio"]["Lacado Mate"])
        cls.vlr_anodizado = str(config["costo_aluminio"]["Anodizado"])
        cls.vlr_transparente = str(config["costo_vidrio"]["Transparente"])
        cls.vlr_bronce = str(config["costo_vidrio"]["Bronce"])
        cls.vlr_azul = str(config["costo_vidrio"]["Azul"])
        cls.vlr_esmerilado = str(config["costo_vidrio"]["Esmerilado"])

        while True:
            if opcion == '1':
                table = Table(title="Tarifas de acabados")

                table.add_column("Descripción", style="cyan", justify="center")
                table.add_column("Precio * m lineal", style="magenta", justify="center")

                table.add_row("Acabado púlido", f"$ {cls.vlr_pulido}")
                table.add_row("Acabado lacado brillante", f"$ {cls.vlr_brillante}")
                table.add_row("Acabado lacado mate", f"$ {cls.vlr_mate}")
                table.add_row("Acabado anodizado", f"$ {cls.vlr_anodizado}")

                console.print(table)
                break
            elif opcion == '2':
                table = Table(title="Tarifas de vidrios")

                table.add_column("Descripción", style="cyan", justify="center")
                table.add_column("Precio * cm2", style="magenta", justify="center")

                table.add_row("Vídrio transparente", f"$ {cls.vlr_transparente}")
                table.add_row("Vídrio bronce", f"$ {cls.vlr_bronce}")
                table.add_row("Vídrio azul", f"$ {cls.vlr_azul}")
                table.add_row("Valor adicional esmerilado", f"$ {cls.vlr_esmerilado}")

                console.print(table)
                break
            elif opcion == '3':
                console.print("[bold green]Volviendo al menú...[/bold green]")
                break
            else:
                console.print("[bold red]¡Opción incorrecta! Intente nuevamente...[/bold red]")