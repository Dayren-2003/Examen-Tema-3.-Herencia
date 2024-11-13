# Importar la clase Planta
from planta import Planta

class PlantaTipo(Planta):
    def __init__(self, nombre, tipo, tamano):
        # Llamar al constructor de la clase padre (Planta)
        super().__init__(nombre, tipo)
        # Atributo adicional de la clase hija
        self.tamano = tamano

    # Método para mostrar la información completa de la planta
    def mostrar_info(self):
        # Llamar al método de la clase padre
        super().mostrar_info()
        # Mostrar el atributo adicional de la clase hija
        print(f"Tamaño: {self.tamano}")
