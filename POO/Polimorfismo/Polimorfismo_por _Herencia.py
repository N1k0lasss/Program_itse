# Polimorfismo por herencia

class Animal:                   # Clase base
    def hablar(self):           # Método base
        pass                    # No retorna valor


class Perro(Animal):            # Clase derivada
    def hablar(self):           # Método heredado
        return "Guau!"          # retorna un valor en este caso "Guau!"

#   Clase derivada


class Gato(Animal):             # Clase derivada
    def hablar(self):           # Método heredado
        return "Miau!"          # retorna un valor en este caso "Miau!"


# Uso polimórfico
animales = [Perro(), Gato()]    # Lista de objetos de diferentes clases

for animal in animales:         # Iteración sobre la lista
    print(animal.hablar())      # Llama al método hablar
