import json
import os
current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, "datos.json")

class Ventana:
    def __init__(self, estilo, ancho, alto, acabado, tipo_vidrio, esmerilado=False):
        # Cargar configuraciones desde el archivo JSON
        with open(json_path, "r") as file:
            config = json.load(file)
        
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.acabado = acabado
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado

        # Cargar valores fijos del JSON
        self.medida_aluminio = config["medidas"]["aluminio"]
        self.medida_vidrio = config["medidas"]["vidrio"]
        self.estilo_naves = config["estilo_naves"]
        self.costo_aluminio = config["costo_aluminio"]
        self.costo_vidrio = config["costo_vidrio"]
        self.esquinas = config["esquinas"]
        self.chapa = config["chapa"]

    def calcular_cantidad_naves(self):
        naves = self.estilo_naves[self.estilo]
        return self.ancho / naves, naves

    def calcular_valor_aluminio(self):
        ancho_nave, _ = self.calcular_cantidad_naves()
        costo_por_cm_lineal = {
            "Pulido": self.costo_aluminio["Pulido"] / self.costo_aluminio["divi_unidad"],
            "Lacado Brillante": self.costo_aluminio["Lacado Brillante"] / self.costo_aluminio["divi_unidad"],
            "Lacado Mate": self.costo_aluminio["Lacado Mate"] / self.costo_aluminio["divi_unidad"],
            "Anodizado": self.costo_aluminio["Anodizado"] / self.costo_aluminio["divi_unidad"]
        }

        ancho_aluminio = ancho_nave - (self.medida_aluminio * 2)
        alto_aluminio = self.alto - (self.medida_aluminio * 2)
        area_aluminio = (2 * ancho_aluminio +  2 * alto_aluminio)
        return area_aluminio * costo_por_cm_lineal[self.acabado]

    def calcular_valor_vidrio(self):
        ancho_nave, _ = self.calcular_cantidad_naves()

        costo_por_cm2 = {
            "Transparente": self.costo_vidrio["Transparente"],
            "Bronce": self.costo_vidrio["Bronce"],
            "Azul": self.costo_vidrio["Azul"]
        }

        ancho_vidrio = ancho_nave - (self.medida_vidrio * 2)
        alto_vidrio = self.alto - (self.medida_vidrio * 2)
        area_vidrio = (ancho_vidrio * alto_vidrio)

        valor_vidrio = area_vidrio * costo_por_cm2[self.tipo_vidrio]

        if self.esmerilado:
            valor_vidrio += area_vidrio * self.costo_vidrio["Esmerilado"]
        return valor_vidrio

    def calcular_valor_esquinas(self):
        return self.esquinas * 4

    def calcular_valor_accesorios(self):
        if "X" in self.estilo:
            return self.chapa
        return 0