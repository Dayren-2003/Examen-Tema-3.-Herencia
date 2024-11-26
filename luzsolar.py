class Luz:
    def __init__(self, luz_solar):
        # Atributos comunes para todas las plantas
        self.luz_solar = luz_solar  # Atributo específico para la luz solar

    # Getter para acceder al atributo luz_solar
    def get_luz_solar(self):
        return self.luz_solar

    # Método para mostrar la información común de las plantas
    def mostrar_info(self):
        print(f"Luz Solar: {self.luz_solar}")
