from flask import Flask, render_template, request, redirect, url_for, jsonify
from ventana import Ventana
from cotizacion import Cotizacion
from cliente import Cliente
import json
import os
current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, "datos.json")

with open(json_path, "r") as file:
    config = json.load(file)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crear_cotizacion", methods=["GET", "POST"])
def crear_cotizacion():
    if request.method == "POST":
        nombre_cliente = request.form["nombre_cliente"]
        empresa_cliente = request.form["empresa_cliente"]
        cantidad_ventanas = int(request.form["cantidad_ventanas"])
        estilo = request.form["estilo"]
        ancho = float(request.form["ancho"])
        alto = float(request.form["alto"])
        acabado = request.form["acabado"]
        tipo_vidrio = request.form["tipo_vidrio"]
        esmerilado = request.form.get("esmerilado") == "on"

        cliente = Cliente(nombre_cliente, empresa_cliente)
        ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado)
        cotizacion = Cotizacion(cliente, ventana, cantidad_ventanas)
        total = cotizacion.calcular_total()

        return render_template("cotizacion.html", cliente=cliente, ventana=ventana, cotizacion=cotizacion, total=total)

    return render_template("crear_cotizacion.html")

@app.route('/ver_tarifas/<opcion>')
def ver_tarifas(opcion):
    tarifas_aluminio = {
        "Pulido": config["costo_aluminio"]["Pulido"],
        "Lacado Brillante": config["costo_aluminio"]["Lacado Brillante"],
        "Lacado Mate": config["costo_aluminio"]["Lacado Mate"],
        "Anodizado": config["costo_aluminio"]["Anodizado"]
    }

    tarifas_vidrio = {
        "Transparente": config["costo_vidrio"]["Transparente"],
        "Bronce": config["costo_vidrio"]["Bronce"],
        "Azul": config["costo_vidrio"]["Azul"],
        "Esmerilado": config["costo_vidrio"]["Esmerilado"]
    }

    if opcion == '1':
        return render_template(
            'tarifas.html', 
            titulo="Tarifas de Acabados",
            tarifas=tarifas_aluminio
        )
    elif opcion == '2':
        return render_template(
            'tarifas.html', 
            titulo="Tarifas de Vidrios",
            tarifas=tarifas_vidrio
        )

if __name__ == "__main__":
    app.run(debug=True)