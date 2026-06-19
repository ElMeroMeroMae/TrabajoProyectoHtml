class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def atacar(self):
        print(f"{self.nombre} realiza un ataque básico.")

class Mago(Personaje):
    def __init__(self, nombre, vida, mana):
        super().__init__(nombre, vida)
        self.mana = mana

    def atacar(self):
        self.mana -= 10
        print(f"{self.nombre} lanza un hechizo. (Mana restante: {self.mana})")

class Guerrero(Personaje):
    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida)
        self.fuerza = fuerza

    def atacar(self):
        print(f"{self.nombre} lanza un ataque físico potente con fuerza {self.fuerza}!")

aventureros = [Mago("Hoodinie", 60, 50), Guerrero("Bombo", 100, 20)]

print("--- ¡Inicia el combate! ---")
for aventurero in aventureros:
    aventurero.atacar()