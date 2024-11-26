class Planta:
    def __init__(self, nombre, tipo):
        # Atributos que definen la planta
        self.nombre = nombre
        self.tipo = tipo

    # Métodos getters para acceder a los atributos
    def get_nombre(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def mostrar_info(self):
        # Método para mostrar la información de la planta
        print(f"\nPlanta: {self.nombre}")
        print(f"Tipo: {self.tipo}")
