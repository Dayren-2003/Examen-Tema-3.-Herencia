from tipo import PlantaTipo

class OrquideaExotica(PlantaTipo):
    def __init__(self, color_flor, tipo_fertilizante, duracion_flor):
        # Llamar al constructor de la clase base con parámetros requeridos
        super().__init__("Orquídea Exótica", "Orquídea",)
        # Inicializar atributos específicos de la orquídea exótica
        self.color_flor = color_flor
        self.tipo_fertilizante = tipo_fertilizante
        self.duracion_flor = duracion_flor

    # Métodos getters para acceder a los atributos
    def get_color_flor(self):
        return self.color_flor

    def get_tipo_fertilizante(self):
        return self.tipo_fertilizante

    def get_duracion_flor(self):
        return self.duracion_flor

    # Métodos para mostrar información específica de la orquídea exótica
    def mostrar_color_flor(self):
        print(f"Color de la flor: {self.color_flor}")

    def mostrar_tipo_fertilizante(self):
        print(f"Tipo de fertilizante: {self.tipo_fertilizante}")

    def mostrar_duracion_flor(self):
        print(f"Duración de la floración: {self.duracion_flor}")

    # Mostrar toda la información de la planta
    def mostrar_info_completa(self):
        # Llamar al método de la clase padre para mostrar la información general
        self.mostrar_info()
        # Mostrar la información específica de la orquídea exótica
        self.mostrar_color_flor()
        self.mostrar_tipo_fertilizante()
        self.mostrar_duracion_flor()
