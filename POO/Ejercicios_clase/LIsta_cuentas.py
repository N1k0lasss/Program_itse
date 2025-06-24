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
