#   CLase de cuenta bancaria
class cuenta_bancaria:
    def __init__(self, nro_cuenta, dni, nombre, apellido, saldo=0, cuenta_corriente=False):
        self.nro_cuenta = nro_cuenta
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

#   Metodo para realizar el deposito
    def deposito(self, cantidad):
        self.saldo += cantidad
        return f"Se ha depositado ${cantidad} al saldo de la cuenta {self.nro_cuenta}"

#   Metodo para realizar la extracción
    def extraccion(self, cantidad):
        if self.cuenta_corriente:
            limite = self.saldo + 10000
            if cantidad > limite:
                return f"No puede extraer más de $10.000 por debajo del saldo. Saldo disponible para extraer: ${limite}"
            self.saldo -= cantidad
            return f"Se ha realizado una extracción de ${cantidad}.\nSaldo actual: ${self.saldo}"
        else:
            if cantidad > self.saldo:
                cantidad = self.saldo
            self.saldo -= cantidad
            return f"Se ha realizado una extracción de ${cantidad}.\nSaldo actual: ${self.saldo}"

#   metodo para imprimir el objeto
    def __str__(self):
        return (
            f"Nro Cuenta: {self.nro_cuenta}\n"
            f"DNI: {self.dni}\n"
            f"Nombre: {self.nombre}\n"
            f"Apellido: {self.apellido}\n"
            f"Saldo: ${self.saldo}\n"
            f"Cuenta Corriente: {self.cuenta_corriente}\n"
        )


#   ingreso de datos
print("INGRESE LOS DATOS DEL DEUDOR")
print("========================================")
nro_cuenta = int(input("\nIngrese el nro de la cuenta: "))
dni = int(input("Ingrese el DNI: "))
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
saldo = 0.0
cuenta_corriente = input(
    "Ingrese si la cuenta es corriente (S/N): ").strip().upper() == "S" and True or False

# creación de la cuenta
cuenta = cuenta_bancaria(nro_cuenta, dni, nombre,
                         apellido, saldo, cuenta_corriente)

# bucle principal
while True:
    # se imprime el menú de opciones
    print("MENU DE OPCIONES")
    print("-------------------------")
    print("\n1. Depositar")
    print("2. Extraccion")
    print("3. Ver saldo de la cuenta")
    print("4. Mostrar datos del titular")
    print("5. Mostrar datos de la cuenta")
    print("6. Salir")
    print("-------------------------")
    opcion = input("Ingrese la opcion deseada: ")

# se utiliza un match-case para manejar las diferentes opciones del menú
    match opcion:
        case "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            print(cuenta.deposito(cantidad))
        case "2":
            cantidad = float(input("Ingrese la cantidad a extraer: "))
            print(cuenta.extraccion(cantidad))
        case "3":
            print(cuenta.saldo)
        case "4":
            print(cuenta.nombre)
            print(cuenta.apellido)
            print(cuenta.dni)
            print(cuenta.nro_cuenta)
        case "5":
            print(cuenta)
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida")


# FIN DEL PROGRAMA
