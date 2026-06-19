class Animal:
    def sonido(self):
        pass
    
class Perro(Animal):
    def sonido(self):
        print("Woof")

class Gato(Animal):
    def sonido(self):
        print("Miau")
        
animales=[Perro(), Gato(), Perro()]
for animal in animales:
    animal.sonido()