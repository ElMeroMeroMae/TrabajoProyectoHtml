class Vehiculo:
    def describir(self):
        return "Este es un vehículo"

class Moto(Vehiculo):
    def __init__(self, marca, tiene_sidecar):
        self.marca = marca
        self.tiene_sidecar = tiene_sidecar

    def describir(self):
        general = super().describir()
        especifico = f"Moto marca {self.marca}, Sidecar: {self.tiene_sidecar}"
        return f"{general}. {especifico}"

class Coche(Vehiculo):
    def __init__(self, num_puertas):
        self.num_puertas = num_puertas

class Camion(Vehiculo):
    def __init__(self, capacidad_carga):
        self.capacidad_carga = capacidad_carga

mi_moto = Moto("Ducati", False)
print(mi_moto.describir())