# Ejemplo de ENCAPSULACIÓN
# Técnica: Encapsulación
# Autor: Jenny Manzano

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def mostrar_saldo(self):
        print("Saldo actual:", self.__saldo)

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes")

cuenta = CuentaBancaria(500)
cuenta.mostrar_saldo()

cuenta.depositar(200)
cuenta.mostrar_saldo()

cuenta.retirar(100)
cuenta.mostrar_saldo()
