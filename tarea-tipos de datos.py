"""
Programa: Conversión de temperatura
Descripción: Este programa convierte una temperatura ingresada en grados Celsius
a grados Fahrenheit, utilizando diferentes tipos de datos en Python.
"""

# Solicitar datos al usuario (string)
nombre_usuario = input("Ingrese su nombre: ")

# Solicitar temperatura en Celsius (float)
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Conversión de Celsius a Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Verificar si la temperatura es mayor a cero (boolean)
es_temperatura_positiva = temperatura_celsius > 0

# Mostrar resultados
print("\nResultados:")
print(f"Usuario: {nombre_usuario}")
print(f"Temperatura en Celsius: {temperatura_celsius} °C")
print(f"Temperatura en Fahrenheit: {temperatura_fahrenheit} °F")
print(f"¿La temperatura es mayor que cero?: {es_temperatura_positiva}")
