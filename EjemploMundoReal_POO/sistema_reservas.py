"""
Caso del mundo real:
Sistema de Reservas de un Hotel

Descripción:
Este programa modela un sistema sencillo de reservas de hotel utilizando
Programación Orientada a Objetos (POO). Se aplican los principios de:
- Abstracción: clases que representan conceptos reales (Hotel, Habitacion, Cliente)
- Encapsulación: atributos y métodos definidos dentro de cada clase
- Modularidad: cada clase cumple una responsabilidad específica
"""

# Clase que representa a un cliente del hotel
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"


# Clase que representa una habitación
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def liberar(self):
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} - {self.tipo} - ${self.precio} - {estado}"


# Clase que representa el hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        for hab in self.habitaciones:
            print(hab)

    def reservar_habitacion(self, numero):
        for hab in self.habitaciones:
            if hab.numero == numero and hab.disponible:
                hab.reservar()
                print(f"Habitación {numero} reservada con éxito")
                return
        print("Habitación no disponible o no existe")


# ------------------
# Uso del sistema
# ------------------

hotel = Hotel("Hotel Central")

# Crear habitaciones
habitacion1 = Habitacion(101, "Simple", 30)
habitacion2 = Habitacion(102, "Doble", 50)

# Agregar habitaciones al hotel
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

# Mostrar estado inicial
hotel.mostrar_habitaciones()

# Reservar una habitación
hotel.reservar_habitacion(101)

# Mostrar estado final
hotel.mostrar_habitaciones()
