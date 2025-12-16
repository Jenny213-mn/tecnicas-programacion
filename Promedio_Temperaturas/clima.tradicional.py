# Programa en Programación Tradicional
# Calcula el promedio semanal de temperaturas
# usando funciones y estructuras básicas

def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas
    de los 7 días de la semana.
    Retorna una lista de temperaturas.
    """
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal
    a partir de una lista de temperaturas.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def main():
    """
    Función principal del programa
    """
    print("Registro semanal de temperaturas")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()
