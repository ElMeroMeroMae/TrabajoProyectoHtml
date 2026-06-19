class Animal:
    def __init__(self, nombre_cientifico, nombre_comun, habitat, estado_conservacion, esperanza_vida):
        self.nombre_cientifico = nombre_cientifico
        self.nombre_comun = nombre_comun
        self.habitat = habitat
        self.estado_conservacion = estado_conservacion
        self.esperanza_vida = esperanza_vida

    def alimentarse(self):
        print(f"El {self.nombre_comun} está buscando comida en el {self.habitat}.")

    def dormir(self, horas):
        print(f"El {self.nombre_comun} está durmiendo por {horas} horas.")

    def moverse(self):
        print(f"El {self.nombre_comun} se está desplazando por su entorno.")

    def informacion_general(self):
        print(f"\n--- Ficha Técnica: {self.nombre_comun} ---")
        print(f"Científico: {self.nombre_cientifico}")
        print(f"Estado: {self.estado_conservacion} | Esperanza de vida: {self.esperanza_vida} años")


class Mamifero(Animal):
    def __init__(self, nombre_cientifico, nombre_comun, habitat, estado_conservacion, esperanza_vida, gestacion, crias, tiene_pelo):
        super().__init__(nombre_cientifico, nombre_comun, habitat, estado_conservacion, esperanza_vida)
        self.periodo_gestacion = gestacion
        self.cantidad_crias_promedio = crias
        self.tiene_pelo = tiene_pelo

    def amamantar(self):
        print(f"La madre {self.nombre_comun} está amamantando a sus crías.")

    def emitir_sonido(self):
        print(f"El {self.nombre_comun} emite un sonido característico de mamífero.")

class Ave(Animal):
    def __init__(self, nombre_cientifico, nombre_comun, habitat, estado_conservacion, esperanza_vida, envergadura, pico, vuela):
        super().__init__(nombre_cientifico, nombre_comun, habitat, estado_conservacion, esperanza_vida)
        self.envergadura_ala = envergadura
        self.tipo_pico = pico
        self.puede_volar = vuela

    def volar(self):
        if self.puede_volar:
            print(f"El {self.nombre_comun} despliega sus alas de {self.envergadura_ala}m y emprende el vuelo.")
        else:
            print(f"Este ave no puede volar.")

    def construir_nido(self):
        print(f"El {self.nombre_comun} está recolectando ramas para su nido.")

    def poner_huevos(self, cantidad):
        print(f"El ave ha puesto {cantidad} huevos en el nido.")


class MonoAullador(Mamifero):
    def __init__(self, nombre_cientifico, nombre_comun, habitat, estado_conservacion, esperanza_vida, gestacion, crias, tiene_pelo, tamaño_grupo, territorio):
        super().__init__(nombre_cientifico, nombre_comun, habitat, estado_conservacion, esperanza_vida, gestacion, crias, tiene_pelo)
        self.tamaño_grupo = tamaño_grupo
        self.territorio = territorio

    def aullar(self):
        print(f"¡UAAA-UUU! El {self.nombre_comun} aúlla fuertemente para comunicarse con su grupo de {self.tamaño_grupo} individuos.")

    def marcar_territorio(self):
        print(f"Marcando el territorio de {self.territorio} en las copas de los árboles.")

class TucanPicoCanoa(Ave):
    def __init__(self, nombre_cientifico, nombre_comun, habitat, estado_conservacion, esperanza_vida, envergadura, pico, vuela, plumaje, dieta):
        super().__init__(nombre_cientifico, nombre_comun, habitat, estado_conservacion, esperanza_vida, envergadura, pico, vuela)
        self.colores_plumaje = plumaje
        self.dieta_especializada = dieta

    def regurgitar_semilla(self):
        print(f"El tucán ha regurgitado una semilla de su dieta de {self.dieta_especializada}, ayudando a la reforestación.")

    def interactuar_pareja(self):
        print(f"El tucán luce su plumaje {self.colores_plumaje} frente a su pareja.")


congo = MonoAullador("Alouatta palliata", "Mono Aullador", "Bosque Nuboso", "Vulnerable", 20, 6, 1, True, 12, "5 hectáreas")

tucan = TucanPicoCanoa("Ramphastos sulfuratus", "Tucán Pico Canoa", "Selva Tropical", "Preocupación menor", 15, 0.5, "Largo y multicolor", True, "Negro con amarillo brillante", "Frutos tropicales")


congo.informacion_general()
congo.moverse()      
congo.amamantar()    
congo.aullar()       

tucan.informacion_general()
tucan.volar()               
tucan.regurgitar_semilla()  