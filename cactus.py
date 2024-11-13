# cactus.py (Clase Hija Cactus)
from tipo import PlantaTipo
from luzsolar import Luz  # Asumiendo que tienes una clase Luz
class Cactus(PlantaTipo, Luz):
    def __init__ (self, nombre, tipo="Cactus Espinoso", color_espinas="Blancas", altura=30, tamano="Pequeño",
                 luz_solar="Alta"):
        # Llamar al constructor de la clase padre (PlantaTipo)
        PlantaTipo.__init__(self, nombre, tipo, tamano)
        # Llamar al constructor de la clase Luz
        Luz.__init__(self, luz_solar)

        # Atributos específicos de Cactus
        self._color_espinas = color_espinas
        self._altura = altura

    # Métodos para mostrar la información específica del cactus
    def mostrar_color_espinas(self):
        print(f"Color de las espinas: {self._color_espinas}")

    def mostrar_altura(self):
        print(f"Altura del cactus: {self._altura} cm")

    def mostrar_info_completa(self):
        # Llamar al método de la clase padre
        self.mostrar_info()
        # Mostrar la información específica del cactus
        self.mostrar_color_espinas()
        self.mostrar_altura()
