class persona():
    nombre = ""
    edad = 0
    dni = 0
    sexo = ""
    peso = 0
    altura = 0.0

    def __init__(self, nombre="", edad=0, DNI=0, sexo="", peso=0, altura=0):
        self.nombre = nombre  # hace referencia al atributo de la clase o al del parametro
        self.edad = edad
        self.dni = DNI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def calcularIMC(self):
        imc = self.peso/(self.altura**2)
        if imc < 20:
            return -1
        elif imc <= 25:
            return 0
        else:
            return 1

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def comprobadordeSexo(self, sexo):
        if self.sexo == sexo:
            return True
        else:
            return False

    def __str__(self):
        return f"nombre:{self.nombre} edad:{self.edad} dni:{self.dni} sexo:{self.sexo} peso:{self.peso} altura:{self.altura}"


nombre = input("Ingrese el nombre")
dni = input("Ingrese dni")
edad = int(input("Ingrese edad"))
sexo = input("Ingrese sexo")
peso = float(input("ingrese peso"))
altura = float(input("Ingrese su altura"))
objetop = persona(nombre, edad, dni, sexo, peso, altura)
while True:
    print("1-Calcular IMC")
    print("2-Es mayor de edad")
    print("3-Comprobar sexo")
    print("4-Imprimir todos los datos")
    print("S-salir")
    opcion = input("Ingrese la opcion deseada")
    match opcion:
        case "1":
            imc = objetop.calcularIMC()
            if imc == -1:
                print("Bajo peso")
            elif imc == 0:
                print("peso normal")
            else:
                print("sobrepeso")
        case "2":
            if objetop.esMayorDeEdad():
                print("Es mayor de edad")
            else:
                print("Es menor de edad")
        case "3":
            sexo = input("Ingrese el sexo: ")
            if objetop.comprobadordeSexo(sexo):
                print("el sexo ingresado es correcto")
            else:
                print("el sexo ingresado es incorrecto")
        case "4":
            print(objetop.__str__())
        case "5":
            break

    pass
