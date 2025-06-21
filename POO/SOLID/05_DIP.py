#   DIP
#   Dependency Inversion Principle (Principio de Inversión de Dependencias)

from abc import ABC, abstractmethod


class verificador_ortografico(ABC):
    @abstractmethod
    def verificar_palabras(self, palabras):
        pass


class diccionario(verificador_ortografico):
    def verificar_palabras(self, palabras):
        # Logica para verificar palabras
        pass


class servicio_online(verificador_ortografico):
    def verificar_palabras(self, palabras):
        # Logica para verificar palabras desde el servicio online
        pass


class corrector_ortografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        # Usamos el verificador para corregir el texto


corrector_ortografico = corrector_ortografico(diccionario())
corrector_ortografico.corregir_texto("Este texto es muy mal")


# Explicación
# La idea es que el corrector ortográfico no se encargue de la verificación de palabras, sino que se encargue de corregir el texto.
# Esto se logra mediante la herencia de la clase corrector_ortografico, que hereda de la clase corrector, y en la clase corrector se define la función corregir_texto, que llama a la función verificar_palabras del objeto verificador.
# En este caso, la función verificar_palabras del objeto verificador se llama desde la función corregir_texto del objeto corrector_ortografico, y la función corregir_texto del objeto corrector se llama desde la función corregir_texto del objeto corrector_ortografico.
# Esto permite que el corrector ortográfico pueda corregir el texto sin tener que verificar las palabras, lo que reduce la complejidad del código y mejora la legibilidad.

# Implementación
# En la clase corrector_ortografico, se define la función corregir_texto, que llama a la función verificar_palabras del objeto verificador.
# En la clase corrector, se define la función corregir_texto, que llama a la función verificar_palabras del objeto verificador.
# En la clase verificador_ortografico, se define la función verificar_palabras, que llama a la función verificar_palabras del objeto verificador.
# En la clase diccionario, se define la función verificar_palabras, que llama a la función verificar_palabras del objeto verificador.
# En la clase servicio_online, se define la función verificar_palabras, que llama a la función verificar_palabras del objeto verificador.
