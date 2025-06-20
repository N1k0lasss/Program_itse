class persona():
    nombre = ""
    edad = 0
    dni = 0
    sexo = ""
    peso = 0.0
    altura = 0

    def __init__(self, nombre="", edad=0, dni=0, sexo="M", peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        if imc < 20:
            return -1
        elif imc <= 25:
            return 0
        else:
            return 1

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def comprobar_sexo(self, sexo):
        return self.sexo.lower() == sexo.lower()

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, dni: {self.dni}, Sexo: {self.sexo}, Peso: {self.peso}, Altura: {self.altura}"


nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))
dni = int(input("Introduce el DNI: "))
sexo = input("Introduce el sexo : ")
peso = float(input("Introduce el peso: "))
altura = float(input("Introduce la altura: "))
objeto_persona = persona(nombre, edad, dni, sexo, peso, altura)

while True:
    print("INGRESE LA OPCION")
    print("1. Calcular IMC")
    print("2. Comprobar si es mayor de edad")
    print("3. Comprobar sexo")
    print("4. Todos los datos")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")
    match opcion:
        case "1":
            imc = objeto_persona.calcular_imc()
            if imc == -1:
                print("Bajo peso")
            elif imc == 0:
                print("Peso normal")
            else:
                print("Sobrepeso")
        case "2":
            if objeto_persona.es_mayor_de_edad():
                print("Es mayor de edad")
            else:
                print("Es menor de edad")
        case "3":
            sexo_input = input("Ingrese el sexo: ")
            if objeto_persona.comprobar_sexo(sexo_input):
                print("El sexo ingresado es correcto")
            else:
                print("El sexo ingresado es incorrecto")
        case "4":
            print(objeto_persona)
        case "5":
            break
        case _:
            print("Opción no válida")
