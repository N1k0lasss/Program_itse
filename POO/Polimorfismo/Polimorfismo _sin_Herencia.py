#   Polimorfismo sin herencia


class Pato:                         # Clase base
    def volar(self):                # Método base
        return "El pato vuela"      # retorna un valor en este caso "El pato vuela"


class Avion:                        # Clase base
    def volar(self):                # Método base
        return "El avión vuela"     # retorna un valor en este caso "El avión vuela"

# Duck typing
# Si un objeto "se comporta como un pato", se puede usar como tal, sin necesidad de herencia explícita.
# Esto se conoce como "Duck typing" o "Polimorfismo sin herencia".


def hacer_volar(objeto):            # Función que recibe un objeto
    print(objeto.volar())           # Llama al método volar


hacer_volar(Pato())                # Llama al método volar de la clase Pato
hacer_volar(Avion())               # Llama al método volar de la clase Avion
