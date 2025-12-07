# Ejemplo de estructuras de control
# Técnica: Condicionales y ciclos
# Autor: Jenny213-mn

numero = int(input("Ingrese un numero: "))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

print("Numeros del 1 al 10:")
for i in range(1, 11):
    print(i)

print("Cuenta regresiva:")
x = 5
while x > 0:
    print(x)
    x -= 1
