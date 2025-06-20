#   OCP
#   Open-Closed Principle (Principio Abierto-Cerrado)
#   Una clase debe tener una responsabilidad abierta para la extensión
#   y cerrada para la modificación

class notificador():
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError


class email(notificador):
    def notificar(self):
        print(f"Enviando Email a {self.usuario}")


class sms(notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario}")


class whatsapp(notificador):
    def notificar(self):
        print(f"Enviando WhatsApp a {self.usuario}")

#   si yo se que en el futuro quiero agregar mas funcionalidades tengo que dejar un sistema abierto
#   para que otros puedan agregar sus propias funcionalidades
#   y no tengo que modificar el código de la clase notificador
