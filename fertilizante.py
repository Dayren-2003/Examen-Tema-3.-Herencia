# orquidea.py (Clase Hija Orquidea)
from tipo import PlantaTipo

class OrquideaExotica(PlantaTipo):
    def __init__(self, nombre, color_flor="Púrpura", tipo_fertilizante="Cada dos semanas", duracion_flor="Ocho semanas",
                 tamano="Pequeña"):
        PlantaTipo.__init__(self, nombre, "Orquídea", tamano)

        # Atributos específicos de la orquídea
        self._color_flor = color_flor
        self._tipo_fertilizante = tipo_fertilizante
        self._duracion_flor = duracion_flor

    def mostrar_color_flor(self):
        print(f"Color de la flor: {self._color_flor}")

    def mostrar_tipo_fertilizante(self):
        print(f"Tipo de fertilizante: {self._tipo_fertilizante}")

    def mostrar_duracion_flor(self):
        print(f"Duración de la floración: {self._duracion_flor}")

    def mostrar_info_completa(self):
        self.mostrar_info()
        self.mostrar_color_flor()
        self.mostrar_tipo_fertilizante()
        self.mostrar_duracion_flor()
