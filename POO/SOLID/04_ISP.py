#   ISP
#   Interface Segregation Principle (Principio de Segregación de Interfaces)
#   Una clase debe ser una interfaz para una colección de clases

from abc import ABC, abstractmethod


class trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass


class humano(trabajador):
    def trabajar(self):
        print("Trabajando")

    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Dormiendo")


class robot(trabajador):
    def trabajar(self):
        print("Trabajando")

    def comer(self):
        pass

    def dormir(self):
        pass


robot = robot()

#   Explicación
#   La clase trabajador es una interfaz para una colección de clases
#   La clase humano y la clase robot son clases que implementan la interfaz trabajador
#   La clase humano implementa las funciones trabajar, comer y dormir
#   La clase robot implementa solo las funciones trabajar
