class Persona: #superclase
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print('hola estoy hablando')

class Empleado(Persona): #subclase, hereda los metodos de la clase Persona
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad) #indica que vamos a heredar de la clase padre
        self.trabajo =  trabajo
        self.salario = salario
    def hablar(self):
        print('ya no estoy hablando') #la clase empleado le asigna un nuevo metodo, distinta a la de la superclase (Persona)
 
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,grado,universidad):
        super().__init__(nombre, edad, nacionalidad) #indica que vamos a heredar de la clase padre
        self.grado =  grado
        self.universidad = universidad
    def hablar(self):
        print('soy un estudiante')
       
        

empleador = Empleado('Nicolas', 18 ,'argentino', 'programador',10000)
estudiante1 = Estudiante('Alfonso',22,'argentino',5,'unse')
print(estudiante1.grado)
estudiante1.hablar()
        
        