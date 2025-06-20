# SRP
# Single Responsibility Principle (Principio de Responsabilidad Única)
# Una clase debe tener una única responsabilidad

class auto():
    # esta clase debe tener una única responsabilidad
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("has movido el auto")
        else:
            return ("No hay suficiente combustible")

    def obtener_posicion(self):
        return self.posicion


class tanque_de_combustible():
    # esta otra clase tiene la responsabilidad de manejar el combustible
    def __init__(self, combustible):
        self.combustible = combustible

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


tanque = tanque_de_combustible(100)
auto = auto(tanque)

print(auto.obtener_posicion())
print(auto.mover(10))
print(auto.obtener_posicion())
print(auto.mover(20))

#   Explicación
#   La clase auto tiene una responsabilidad única
#   La clase tanque_de_combustible tiene una responsabilidad única
#   La clase auto y la clase tanque_de_combustible son clases que implementan la responsabilidad única


#   Mas datos a saber
#   No sobrecargar las clases con métodos
#   que no tienen una responsabilidad
#   de este modo el codigo queda más limpio y organizado
#   y es mas fácil de mantener y modificar
