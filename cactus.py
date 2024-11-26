# cactus.py
from tipo import PlantaTipo


class Cactus(PlantaTipo):
    def __init__(self, nombre, resistencia_sequia, almacenamiento_agua):
        # Llamar al constructor de la clase base con parámetros requeridos
        super().__init__(nombre, "Cactus")

        # Atributos relacionados con la resistencia a la sequía y almacenamiento de agua
        self.resistencia_sequia = resistencia_sequia  # Resistencia a la sequía del cactus
        self.almacenamiento_agua = almacenamiento_agua  # Capacidad de almacenamiento de agua del cactus

    # Métodos getters para acceder a los atributos
    def get_resistencia_sequia(self):
        return self.resistencia_sequia

    def get_almacenamiento_agua(self):
        return self.almacenamiento_agua

    # Métodos para mostrar información específica del cactus
    def mostrar_resistencia_sequia(self):
        print(f"Resistencia a la sequía: {self.resistencia_sequia}")

    def mostrar_almacenamiento_agua(self):
        print(f"Almacenamiento de agua: {self.almacenamiento_agua}")

    # Mostrar toda la información del cactus
    def mostrar_info_completa(self):
        # Llamar al método de la clase padre para mostrar la información general
        self.mostrar_info()
        # Mostrar la información específica del cactus
        self.mostrar_resistencia_sequia()
        self.mostrar_almacenamiento_agua()
