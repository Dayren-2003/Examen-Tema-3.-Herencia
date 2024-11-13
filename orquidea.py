# orquidea.py (Clase Hija Orquidea)
from tipo import PlantaTipo


class Orquidea(PlantaTipo):
    def __init__(self, nombre, color_flor="Púrpura", tipo_fertilizante="Cada dos semanas", duracion_flor="Ocho semanas",
                 tamano="Pequeña"):
        # Llamar al constructor de la clase padre (PlantaTipo)
        PlantaTipo.__init__(self, nombre, "Orquídea", tamano)

        # Atributos específicos de la orquídea
        self._color_flor = color_flor
        self._tipo_fertilizante = tipo_fertilizante
        self._duracion_flor = duracion_flor

    # Métodos para mostrar información específica de la orquídea
    def mostrar_color_flor(self):
        print(f"Color de la flor: {self._color_flor}")

    def mostrar_tipo_fertilizante(self):
        print(f"Tipo de fertilizante: {self._tipo_fertilizante}")

    def mostrar_duracion_flor(self):
        print(f"Duración de la floración: {self._duracion_flor}")

    def mostrar_info_completa(self):
        # Llamar al método de la clase padre
        self.mostrar_info()
        # Mostrar la información específica de la orquídea
        self.mostrar_color_flor()
        self.mostrar_tipo_fertilizante()
        self.mostrar_duracion_flor()
