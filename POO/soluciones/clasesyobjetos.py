# Definimos una clase llamada Celular
class Celular:
    # Método constructor: se ejecuta cuando se crea un nuevo objeto
    def __init__(self,marca,modelo,camara): #Todos los def dentro de una clase que utiliicemos, son metodos
        #self representa al objeto actual que se esta creando
        # los atributos 'marca', 'modelo', y 'camara' se asignal al objeto usando self
        self.marca = marca
        self.modelo = modelo # 'self.modelo' pertenece al objeto, 'modelo' es el parámetro
        self.camara = camara
    def Llamar(self): #siempre poner el self
        print(f'Iniciaste una llamada de un: {self.modelo}') #siempre colocar el self
    def Cortar(self):
        print(f'cortaste la llamada desde un: {self.modelo}')

celular1 = Celular('Samsung','s23', '48')
celular2 = Celular('Apple','15','48MP')
print(celular2.Cortar())