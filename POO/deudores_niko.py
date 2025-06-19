
#   el import de la librería datetime para manejar fechas
from datetime import datetime

#   Clase para representar un deudor


class Deudor:
    def __init__(self, dni=0, apellido="", nombre="", dni_cotitular=0, apellido_cotitular="", nombre_cotitular="", monto_deudado=0.0, año_deudado=0):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.dni_cotitular = dni_cotitular
        self.apellido_cotitular = apellido_cotitular
        self.nombre_cotitular = nombre_cotitular
        self.monto_deudado = monto_deudado
        self.año_deudado = año_deudado


#   Método para calcular la deuda actual considerando el interés del 21% anual

    def calcular_deuda_actual(self):
        año_actual = datetime.now().year
        años_transcurridos = año_actual - self.año_deudado
        monto_actual = self.monto_deudado * ((1 + 0.21) ** años_transcurridos)
        return round(monto_actual, 2)


#   Método para realizar el plan de pago (ajustado a la deuda actual)

    def realizar_plan_pago(self, cantidad_cuotas):
        deuda_actual = self.calcular_deuda_actual()
        if cantidad_cuotas < 1 or cantidad_cuotas > 12:
            return "Cantidad de cuotas no válida, debe ser entre 1 y 12"
        cuota_base = deuda_actual / cantidad_cuotas
        interes_cuotas = 0
        if cantidad_cuotas > 3 and cantidad_cuotas <= 6:
            interes_cuotas = 0.09
        elif cantidad_cuotas > 6 and cantidad_cuotas <= 12:
            interes_cuotas = 0.19
        cuota_final = cuota_base * (1 + interes_cuotas)
        return f"{cantidad_cuotas} cuotas de ${cuota_final:.2f} cada una (interés aplicado: {interes_cuotas*100:.0f}%)"


#   Metodo para cambiar el cotitular

    def cambiar_cotitular(self):
        self.dni_cotitular = int(input('Ingrese el DNI del cotitular: '))
        self.nombre_cotitular = input('Ingrese el nombre del cotitular: ')
        self.apellido_cotitular = input('Ingrese el apellido del cotitular: ')
        self.monto_deudado *= 1.5  # Aumenta el monto de la deuda al cambiar cotitular
        print(
            f"\nCotitular cambiado correctamente. Nuevo cotitular: El/La señor/a {self.apellido_cotitular} {self.nombre_cotitular} Con DNI: {self.dni_cotitular}")


#   Metodo para imprimir el objeto

    def __str__(self):
        return (
            f"\nDNI: {self.dni}\n"
            f"Apellido: {self.apellido}\n"
            f"Nombre: {self.nombre}\n"
            f"DNI Cotitular: {self.dni_cotitular}\n"
            f"Apellido Cotitular: {self.apellido_cotitular}\n"
            f"Nombre Cotitular: {self.nombre_cotitular}\n"
            f"Monto Deudado: ${self.monto_deudado}\n"
            f"Año Deudado: {self.año_deudado}\n"
        )


#   Ingreso de Datos
print("INGRESE LOS DATOS DEL DEUDOR")
print("========================================")

#   Ingreso de Datos del deudor
dni = int(input("\nIngrese el DNI del deudor: "))
apellido = input("Ingrese el apellido del deudor: ")
nombre = input("Ingrese el nombre del deudor: ")

#   Ingreso de Datos del cotitular
#   Se asume que el cotitular es obligatorio, por lo que se solicita su información
print("\nINGRESE LOS DATOS DEL COTITULAR")
print("==================================")
dni_cotitular = int(input("\nIngrese el DNI del cotitular: "))
apellido_cotitular = input("Ingrese el apellido del cotitular: ")
nombre_cotitular = input("Ingrese el nombre del cotitular: ")

#   Ingreso del monto adeudado y el año de la deuda
print("\nIngrese el monto adeudado y el año de la deuda")
print("===============================================")
monto_deudado = float(input("\nIngrese el monto deudado: "))
año_deudado = int(input("Ingrese el año deudado: "))


#   Creación del objeto Deudor con los datos ingresados
#   Se utiliza el constructor de la clase Deudor para crear una instancia de Deudor
deudor1 = Deudor(dni, apellido, nombre, dni_cotitular,
                 apellido_cotitular, nombre_cotitular, monto_deudado, año_deudado)

#   Variable para almacenar la deuda actual
#   Inicialmente se establece en None para indicar que aún no se ha calculado
deuda_actual = None

#   Bucle principal del menú de opciones
#   Se utiliza un bucle infinito para mostrar el menú y permitir al usuario seleccionar opciones
while True:
    print("-------------------------")
    print("\n--- MENÚ DE OPCIONES ---")
    print("n\1-Calcular deuda actual")
    print("2-Cambiar cotitular")
    print("3-Realizar plan de pago")
    print("4-Imprimir todos los datos")
    print("0-Salir")
    print("-------------------------")
    opcion = input("Ingrese la opcion deseada: ")


#   Se utiliza un match-case para manejar las diferentes opciones del menú
#   Dependiendo de la opción seleccionada, se ejecuta una acción específica
    match opcion:
        case "1":
            deuda_actual = deudor1.calcular_deuda_actual()
            print(f"\nLa deuda actual es de ${deuda_actual:.2f}\n")
        case "2":
            deudor1.cambiar_cotitular()
            print("Cotitular cambiado exitosamente.")
            print(deudor1)
        case "3":
            if deuda_actual is None:
                print("Primero debe calcular la deuda actual (opción 1).")
            else:
                cantidad_cuotas = int(
                    input("Ingrese la cantidad de cuotas (1 a 12): "))
                print(deudor1.realizar_plan_pago(cantidad_cuotas))
        case "4":
            print(deudor1)
        case "0":
            print("-------------------------")
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida")

#   Fin del bucle principal del menú de opciones
#   El programa continuará ejecutándose hasta que el usuario seleccione la opción de salir (0)
#   Se imprime un mensaje de despedida al salir del programa
#   FIN DEL PROGRAMA
