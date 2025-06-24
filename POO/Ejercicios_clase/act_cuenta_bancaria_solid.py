class CuentaBancaria:
    def __init__(self, nro_cuenta, dni, nombre, apellido, saldo=0):
        self.nro_cuenta = nro_cuenta
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = saldo


class CajaDeAhorro(CuentaBancaria):
    def deposito(self, cantidad):
        self.saldo += cantidad
        return f"Se ha depositado ${cantidad} al saldo de la cuenta {self.nro_cuenta}"

    def extraccion(self, cantidad):
        if cantidad > self.saldo:
            cantidad = self.saldo
        self.saldo -= cantidad
        return f"Se ha realizado una extracción de ${cantidad}.\nSaldo actual: ${self.saldo}"

    def __str__(self):
        return (
            f"Nro Cuenta: {self.nro_cuenta}\n"
            f"DNI: {self.dni}\n"
            f"Nombre: {self.nombre}\n"
            f"Apellido: {self.apellido}\n"
            f"Saldo: ${self.saldo}\n"
            f"Tipo: Caja de Ahorro\n"
        )


class CuentaCorriente(CuentaBancaria):
    def deposito(self, cantidad):
        self.saldo += cantidad
        return f"Se ha depositado ${cantidad} al saldo de la cuenta {self.nro_cuenta}"

    def extraccion(self, cantidad):
        limite = self.saldo + 10000
        if cantidad > limite:
            return f"No puede extraer más de $10.000 por debajo del saldo. Saldo disponible para extraer: ${limite}"
        self.saldo -= cantidad
        return f"Se ha realizado una extracción de ${cantidad}.\nSaldo actual: ${self.saldo}"

    def __str__(self):
        return (
            f"Nro Cuenta: {self.nro_cuenta}\n"
            f"DNI: {self.dni}\n"
            f"Nombre: {self.nombre}\n"
            f"Apellido: {self.apellido}\n"
            f"Saldo: ${self.saldo}\n"
            f"Tipo: Cuenta Corriente\n"
        )


def ingresar_datos_cuenta():
    print("\nINGRESAR DATOS DE LA CUENTA")
    print("================")
    nro_cuenta = int(input("Ingrese el nro de la cuenta: "))
    dni = int(input("Ingrese el DNI: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    tipo = input(
        "Ingrese tipo de cuenta (C: Corriente / A: Ahorro): ").strip().upper()
    saldo = 0.0
    return nro_cuenta, dni, nombre, apellido, tipo, saldo


def main():
    nro_cuenta, dni, nombre, apellido, tipo, saldo = ingresar_datos_cuenta()
    if tipo == "C":
        cuenta = CuentaCorriente(nro_cuenta, dni, nombre, apellido, saldo)
    else:
        cuenta = CajaDeAhorro(nro_cuenta, dni, nombre, apellido, saldo)

    while True:
        print("\nMENU DE OPCIONES")
        print("================")
        print("1. Depositar")
        print("2. Extraer")
        print("3. Ver saldo")
        print("4. Mostrar datos del titular")
        print("5. Mostrar todos los datos")
        print("6. Salir")
        print("================")
        opcion = int(input("Elija una opción: "))

        match opcion:
            case 1:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                print(cuenta.deposito(cantidad))
            case 2:
                cantidad = float(input("Ingrese la cantidad a extraer: "))
                print(cuenta.extraccion(cantidad))
            case 3:
                print(f"Saldo: ${cuenta.saldo}")
            case 4:
                print(f"Nro Cuenta: {cuenta.nro_cuenta}")
                print(f"DNI: {cuenta.dni}")
                print(f"Nombre: {cuenta.nombre}")
                print(f"Apellido: {cuenta.apellido}")
            case 5:
                print(cuenta)
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()
