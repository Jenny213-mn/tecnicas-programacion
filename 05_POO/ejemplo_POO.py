# Ejemplo de Programación Orientada a Objetos en Python
# Técnica: POO
# Autor: Jenny213-mn

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    def es_mayor(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

persona1 = Persona("Carlos", 20)

persona1.mostrar_info()
persona1.es_mayor()
