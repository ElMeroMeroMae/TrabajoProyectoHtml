class Estudiante: 
    def __init__(self, nombre, carrera):
        self.nombre= nombre
        self.carrera= carrera 
    def estudiar(self):
        print("Estudiando")
    def presentar_examen(self):
        print ("En examen")
        
est = Estudiante("Luis", "Sistemas")
est.estudiar()
est.presentar_examen()