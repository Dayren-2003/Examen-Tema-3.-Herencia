# orquidea.py
from tipo import PlantaTipo

class OrquideaExotica(PlantaTipo):
    def __init__(self, nombre, exotica, raices_aereas,):
        # Llamar al constructor de la clase base con parámetros requeridos
        super().__init__(nombre, "Orquídea")

        # Atributos relacionados con las características específicas de la orquídea exótica
        self.exotica = exotica  # Indica si la orquídea es exótica
        self.raices_aereas = raices_aereas  # Indica si tiene raíces aéreas

    # Métodos getters para acceder a los atributos
    def get_exotica(self):
        return self.exotica

    def get_raices_aereas(self):
        return self.raices_aereas

    # Métodos para mostrar información específica de la orquídea exótica
    def mostrar_exotica(self):
        print(f"Exótica: {self.exotica}")

    def mostrar_raices_aereas(self):
        print(f"Raíces aéreas: {self.raices_aereas}")

    # Mostrar toda la información de la planta
    def mostrar_info_completa(self):
        # Llamar al método de la clase padre para mostrar la información general
        self.mostrar_info()
        # Mostrar la información específica de la orquídea exótica
        self.mostrar_exotica()
        self.mostrar_raices_aereas()
