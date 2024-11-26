# Importar la clase Planta
from planta import Planta

class PlantaTipo(Planta):
    def __init__(self, nombre, tipo):
        # Llamar al constructor de la clase padre (Planta)
        super().__init__(nombre, tipo)

    # Método para mostrar la información completa de la planta
    def mostrar_info(self):
        # Llamar al método de la clase padre
        super().mostrar_info()

