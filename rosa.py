# rosa.py (Clase Hija Rosa)
from tipo import PlantaTipo


class Rosa(PlantaTipo):
    def __init__(self, nombre, color_flor="Roja", aroma="Fuerte", florece_en="Primavera", tamano="Mediana"):
        # Llamar al constructor de la clase padre (PlantaTipo)
        PlantaTipo.__init__(self, nombre, "Rosa", tamano)

        # Atributos específicos de la rosa
        self._color_flor = color_flor
        self._aroma = aroma
        self._florece_en = florece_en

    # Métodos para mostrar información específica de la rosa
    def mostrar_color_flor(self):
        print(f"Color de la flor: {self._color_flor}")

    def mostrar_aroma(self):
        print(f"Aroma: {self._aroma}")

    def mostrar_florece_en(self):
        print(f"Florece en: {self._florece_en}")

    def mostrar_info_completa(self):
        # Llamar al método de la clase padre
        self.mostrar_info()
        # Mostrar la información específica de la rosa
        self.mostrar_color_flor()
        self.mostrar_aroma()
        self.mostrar_florece_en()
