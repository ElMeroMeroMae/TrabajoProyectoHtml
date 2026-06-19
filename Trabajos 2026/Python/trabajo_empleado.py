class Empleado:
    def __init__(self, nombre, id, sueldo_base):
        self.nombre = nombre
        self.id = id
        self.sueldo_base = sueldo_base

    def calcular_pago(self):
        return self.sueldo_base

class Vendedor(Empleado):
    def __init__(self, nombre, id, sueldo_base, comision):
        super().__init__(nombre, id, sueldo_base)
        self.comision = comision

    def calcular_pago(self):
        return self.sueldo_base + self.comision