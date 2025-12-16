"""
Caso del mundo real:
Sistema de Biblioteca

Descripción:
Este sistema permite modelar una biblioteca donde los usuarios pueden pedir libros prestados.
"""

# Clase que representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no está prestado.")

# Clase que representa un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def pedir_libro(self, libro):
        libro.prestar()
        if not libro.prestado:
            return
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        libro.devolver()
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

# Crear libros
libro1 = Libro("1984", "George Orwell")
libro2 = Libro("El Hobbit", "J.R.R. Tolkien")

# Crear usuario
usuario = Usuario("Ana")

# Prestar y devolver libros
usuario.pedir_libro(libro1)
usuario.pedir_libro(libro2)

# Devolver un libro
usuario.devolver_libro(libro1)
