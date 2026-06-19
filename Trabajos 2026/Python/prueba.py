class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def mostrarinfo(self):
        print (f"Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera=carrera
        
    def mostrarinfor(self):
        super().mostrarinfo()
        print (f"Carrera: {self.carrera}")

est=Estudiante("Luis", 44, "Sistemas")
est.mostrarinfor
