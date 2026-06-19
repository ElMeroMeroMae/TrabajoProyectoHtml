class Contacto:
    def __init__(self, telefono, correo):
        self.telefono = telefono
        self.correo = correo

directorio = {
    "Juan": Contacto("8888-1111", "juan@correo.com"),
    "Maria": Contacto("7777-2222", "maria@correo.com")
}

# Acceso rápido por nombre
print(f"El tel de Juan es: {directorio['Juan'].telefono}")