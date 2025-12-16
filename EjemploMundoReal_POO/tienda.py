"""
Caso del mundo real:
Sistema de Tienda

Descripción:
Este sistema permite modelar una tienda donde los clientes compran productos.
"""

# Clase que representa un producto en la tienda
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

# Clase que representa un cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_a_carrito(self, producto):
        self.carrito.append(producto)

    def ver_carrito(self):
        print(f"Carrito de {self.nombre}:")
        for producto in self.carrito:
            print(producto)

    def total(self):
        return sum([producto.precio for producto in self.carrito])

# Crear productos
producto1 = Producto("Camiseta", 20)
producto2 = Producto("Pantalón", 30)

# Crear cliente
cliente = Cliente("Juan")

# Agregar productos al carrito
cliente.agregar_a_carrito(producto1)
cliente.agregar_a_carrito(producto2)

# Ver carrito y total
cliente.ver_carrito()
print(f"Total a pagar: ${cliente.total()}")
