# Importar clases de cada "PY" que forman el proyecto
from ventana import Ventana
from cotizacion import Cotizacion
from cliente import Cliente
# Importar biblioteca "Rich"
from rich.console import Console
from rich.prompt import Prompt

console = Console()

# Función para implementar las opciones del menú
def mostrar_menu():
    console.print("\n[bold cyan]/*/*/*/*/*/*/*/- Menú Cotización PQR -/*/*/*/*/*/*/*/[/bold cyan]")
    console.print("[green]1. Crear cotización[/green]")
    console.print("[green]2. Ver tarifas[/green]")
    console.print("[green]3. Salir[/green]")

def crear_cotizacion():
    # Preguntas para recopilación de información
    nombre_cliente = Prompt.ask("[bold]Ingrese el nombre del cotizante[/bold]")
    empresa_cliente = Prompt.ask("[bold]Ingrese el nombre de la empresa[/bold]")
    cantidad_ventanas = int(Prompt.ask("[bold]Ingrese la cantidad de ventanas[/bold]"))
    estilo = Prompt.ask("[bold]Ingrese el estilo de la ventana: \n1. O\n2. XO \n3. OXO \n4. OXXO \n[/bold]")
    ancho = float(Prompt.ask("[bold]Ingrese el ancho de la ventana (cm)[/bold]"))
    alto = float(Prompt.ask("[bold]Ingrese el alto de la ventana (cm)[/bold]"))
    acabado = Prompt.ask("[bold]Ingrese el tipo de acabado: \n1.Pulido \n2.Lacado Brillante \n3.Lacado Mate \n4.Anodizado \n[/bold]")
    tipo_vidrio = Prompt.ask("[bold]Ingrese el tipo de vidrio: \n1.Transparente \n2.Bronce \n3.Azul \n[/bold]")
    esmerilado = Prompt.ask("[bold]Esmerilado (S/N)?[/bold]").lower() == 's'
    
    # Conversión de los valores suministrados: estilo, acabado y tipo de vidrio
    if estilo == "1":
        estilo = "O"
    elif estilo == "2":
        estilo = "XO"
    elif estilo == "3":
        estilo = "OXO"
    elif estilo == "4":
        estilo = "OXXO"

    if acabado == "1":
        acabado = "Pulido"
    elif acabado == "2":
        acabado = "Lacado Brillante"
    elif acabado == "3":
        acabado = "Lacado Mate"
    elif acabado == "4":
        acabado = "Anodizado"

    if tipo_vidrio == "1":
        tipo_vidrio = "Transparente"
    elif tipo_vidrio == "2":
        tipo_vidrio = "Bronce"
    elif tipo_vidrio == "3":
        tipo_vidrio = "Azul"

    # Envío de atributos a clases
    cliente = Cliente(nombre_cliente, empresa_cliente)
    ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado)
    cotizacion = Cotizacion(cliente, ventana, cantidad_ventanas)
    total = cotizacion.calcular_total()

    # Imprimir resultados de la cotización
    console.print(cotizacion.mostrar_cotizacion())
    console.print(f"Precio total de la cotización: ${total}")

def main():
    while True:
        mostrar_menu()
        opcion = Prompt.ask("[bold]Seleccione una opción[/bold]")
        if opcion == '1':
            crear_cotizacion()
        if opcion == '2':
            console.print("\n[bold cyan]¿Qué tarifas deseas ver?:[/bold cyan]")
            console.print("[green]1. Acabados[/green]")
            console.print("[green]2. Vidrios[/green]")
            console.print("[green]3. Volver[/green]")

            opcion_tarifas = Prompt.ask("[bold]Seleccione una opción[/bold]")
            if opcion_tarifas == '1':
                Cotizacion.mostrar_tarifas(opcion_tarifas)
            elif opcion_tarifas == '2':
                Cotizacion.mostrar_tarifas(opcion_tarifas)
            elif opcion_tarifas == '3':
                Cotizacion.mostrar_tarifas(opcion_tarifas)
                mostrar_menu()
            else: 
                console.print("[bold red]¡Opción incorrecta! Intente nuevamente...[/bold red]")
        elif opcion == '3':
            console.print("[bold green]Saliendo del programa...[/bold green]")
            break
        else:
            console.print("[bold red]¡Opción incorrecta! Intente nuevamente...[/bold red]")

if __name__ == "__main__":
    main()