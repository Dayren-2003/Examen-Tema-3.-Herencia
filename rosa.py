# rosa.py (Clase Hija Rosa)
from tipo import PlantaTipo

class Rosa(PlantaTipo):
    def __init__(self, nombre, uso_cosmetico, uso_simbolico):
        # Llamar al constructor de la clase padre (PlantaTipo)
        PlantaTipo.__init__(self, nombre, "Rosa")

        # Atributos específicos de la rosa relacionados con el uso cosmético y simbólico
        self.uso_cosmetico = uso_cosmetico  # Uso cosmético de la rosa
        self.uso_simbolico = uso_simbolico  # Uso simbólico de la rosa

    # Getters para acceder a los atributos
    def get_uso_cosmetico(self):
        return self.uso_cosmetico

    def get_uso_simbolico(self):
        return self.uso_simbolico

    # Métodos para mostrar información específica sobre los usos
    def mostrar_uso_cosmetico(self):
        print(f"Uso Cosmético: {self.uso_cosmetico}")

    def mostrar_uso_simbolico(self):
        print(f"Uso Simbólico: {self.uso_simbolico}")

    # Mostrar toda la información de la rosa
    def mostrar_info_completa(self):
        # Llamar al método de la clase padre para mostrar la información general
        self.mostrar_info()
        # Mostrar la información específica sobre los usos
        self.mostrar_uso_cosmetico()
        self.mostrar_uso_simbolico()
