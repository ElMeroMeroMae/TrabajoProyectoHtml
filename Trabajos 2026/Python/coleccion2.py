class Estudiante:
    def __init__(self, carnet, nombre, carrera, asignaturas):
        self.carnet = carnet
        self.nombre = nombre
        self.carrera = carrera
        self.asignaturas = set(asignaturas) 

class Registro:
    def __init__(self):
        self.estudiantes = []
        self.carnets_existentes = set() 
        self.por_carrera = {}           

    def registrar(self, est):
        if est.carnet in self.carnets_existentes:
            return "Error: Carnet duplicado"
        
        self.estudiantes.append(est)
        self.carnets_existentes.add(est.carnet)
        
        if est.carrera not in self.por_carrera:
            self.por_carrera[est.carrera] = []
        self.por_carrera[est.carrera].append(est)
        return "Registrado con éxito"

    def reporte_general(self):
        self.estudiantes.sort(key=lambda x: x.nombre)
        for e in self.estudiantes:
            print(f"{e.nombre} - {e.carrera} ({e.carnet})")

reg = Registro()
print(reg.registrar(Estudiante("2026-01", "Panchito", "Sistemas", ["Python", "SQL"])))