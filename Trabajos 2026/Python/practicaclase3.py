class Vehiculo:
    def __init__(self, marca, modelo, combustible):
        self.marca=marca
        self.modelo=modelo
        self.combustible=combustible
    def conducir(self, distancia):
        distanciatemp=0
        while distanciatemp!=distancia:
            if distanciatemp/10==int:
                self.combustible-=1
auto_urbano=Vehiculo("Toyota", "Corola", 50)
camioneta=Vehiculo("Ford","F-150", 100)
deportivo=Vehiculo("Ferrari", "Ferrari", 80)
auto_urbano.conducir(300)
camioneta.conducir(300)
deportivo.conducir(300)
