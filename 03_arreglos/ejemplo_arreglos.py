# Ejemplo de arreglos en Python
# Técnica: Arreglos
# Autor: Jenny213-mn

numeros = []

for i in range(5):
    valor = int(input("Ingrese un numero: "))
    numeros.append(valor)

print("Lista completa:", numeros)

print("Numeros pares:")
for n in numeros:
    if n % 2 == 0:
        print(n)

print("Suma de los numeros:", sum(numeros))
