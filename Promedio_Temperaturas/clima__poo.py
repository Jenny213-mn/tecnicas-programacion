# Programa usando Programación Orientada a Objetos (POO)
# Calcula el promedio semanal de temperaturas
# aplicando encapsulamiento y métodos de clase

class ClimaDiario:
    """
    Clase que representa el clima diario
    """

    def __init__(self):
        # Atributo encapsulado (privado)
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas
        de los 7 días de la semana
        """
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        """
        Método para calcular el promedio semanal
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)


# Programa principal
def main():
    print("Registro semanal de temperaturas (POO)")
    
    clima = ClimaDiario()  # Creación del objeto
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio_semanal()
    
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()
