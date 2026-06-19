class Notificacion:
    def enviar(self, mensaje):
        pass 

class Email(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando Email: {mensaje}")

class SMS(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

class Push(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando Notificación Push: {mensaje}")

notificaciones = [Email(), SMS(), Push()]

for n in notificaciones:
    n.enviar("Alerta de seguridad")