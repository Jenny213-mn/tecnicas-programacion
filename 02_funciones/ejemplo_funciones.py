# Ejemplo de funciones en Python
# Técnica: Funciones
# Autor: Jenny213-mn

def suma(a, b):
    return a + b

def cuadrado(x):
    return x * x

def menu():
    print("MENU")
    print("1. Sumar")
    print("2. Calcular cuadrado")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        a = int(input("Ingrese a: "))
        b = int(input("Ingrese b: "))
        print("Resultado:", suma(a, b))

    elif opcion == "2":
        x = int(input("Ingrese un numero: "))
        print("Resultado:", cuadrado(x))

    else:
        print("Opcion invalida")

menu()
