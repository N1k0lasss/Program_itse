from datetime import date


class Cuenta:
    def __init__(self, nroDeCuenta, dniTitular, fehcaApertura, activa, saldo)

    def __str__(self):
        return "Cuenta: " + self.nroDeCuenta + " Titular: " + self.dniTitular + " Fecha de apertura: " + self.fechaApertura + " Activa: " + self.activa + " Saldo: " + self.saldo


class ListaCuentas:
    def __init__(self):
        self.cuentas = []

    def agregarCuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminarCuenta(self, cuenta):
        self.cuentas.remove(cuenta)

    def mostrarCuentas(self):
        for cuenta in self.cuentas:
            print(cuenta)

    def __str__(self):
        return "Lista de cuentas: " + str(self.cuentas)


class Operaciones:
    def __init__(self):
        self.lista = ListaCuentas()

    def depositos(self, nroDeCuenta, monto):
        cuenta = self.lista.cuentas[nroDeCuenta]
        cuenta.saldo += monto
        self.lista.agregarCuenta(cuenta)

    def extracciones(self, nroDeCuenta, monto):
        cuenta = self.lista.cuentas[nroDeCuenta]
        cuenta.saldo -= monto
        self.lista.agregarCuenta(cuenta)

    def saldo(self, nroDeCuenta):
        cuenta = self.lista.cuentas[nroDeCuenta]
        return cuenta.saldo

    def __str__(self):
        return "Lista de cuentas: " + str(self.lista)


def menu():
    print("1. Agregar cuenta")
    print("2. Eliminar cuenta")
    print("3. Mostrar cuentas")
    print("4. Depositar")
    print("5. Extraccion")
    print("6. Saldo")
    print("7. Salir")
    opcion = int(input("Opcion: "))


match opcion:
    case 1:
        nroDeCuenta = int(input("Numero de cuenta: "))
        dniTitular = input("DNI titular: ")
        fechaApertura = date.today()
        activa = bool(input("Activa: "))
        saldo = float(input("Saldo: "))
        cuenta = Cuenta(nroDeCuenta, dniTitular, fechaApertura, activa, saldo)
        lista.agregarCuenta(cuenta)

    case 2:
        nroDeCuenta = int(input("Numero de cuenta: "))
        lista.eliminarCuenta(nroDeCuenta)

    case 3:
        lista.mostrarCuentas()

    case 4:
        nroDeCuenta = int(input("Numero de cuenta: "))
        monto = float(input("Monto a depositar: "))
        operaciones.depositos(nroDeCuenta, monto)

    case 5:
        nroDeCuenta = int(input("Numero de cuenta: "))
        monto = float(input("Monto a extraccion: "))
        operaciones.extracciones(nroDeCuenta, monto)

    case 6:
        nroDeCuenta = int(input("Numero de cuenta: "))
        print(operaciones.saldo(nroDeCuenta))

    case 7:
        exit()

menu()
