# Ejemplo de HERENCIA
# Técnica: Herencia
# Autor: Jenny Manzano

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print("Hola, soy", self.nombre)

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

    def info(self):
        print("Carrera:", self.carrera)

alumno = Estudiante("Ana", "Sistemas")
alumno.presentarse()
alumno.info()
