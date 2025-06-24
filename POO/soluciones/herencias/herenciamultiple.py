class Persona: #superclase
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print('hola estoy hablando')

class Artista: #subclase, hereda los metodos de la clase Persona
    def __init__(self,,habilidad):
        self.habilidad = habilidad
    def mostrarhabilidad(self):
        print(f'mi habilidad es: {self.habilidad}')

class EmpleadoArtista(Persona,Artista): #Herencia multiple
    def __init__(self, nombre, edad, nacionalidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad=)
        self.salario = salario
        self.empresa = empresa