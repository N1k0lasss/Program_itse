class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def Estudiar(self):
        print('esta estudiando')

nombre = input('ingresa tu nombre: ')
edad = input('ingresa tu edad: ')
grado = input('ingresa tu grado: ')

estudiante = Estudiante(nombre,edad,grado)

print(f'''
      Datos del estudiante 
      Nombre:{estudiante.nombre}
      Edad: {estudiante.edad}
      Grado: {estudiante.grado}''')

while True:
    estudiar = input()
    if (estudiar.lower() == 'estudiar'):
        estudiante.Estudiar()