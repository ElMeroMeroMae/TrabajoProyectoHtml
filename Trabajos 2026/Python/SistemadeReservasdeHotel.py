# Carlos David Pravia Herrera y Angel Ramon Gavarrete Munguia

class HabitacionHotel:
    def __init__(self, numero, tipo, ocupada=False):
        self.numero = numero
        self.tipo = tipo
        self.ocupada = ocupada

    def ocupar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f"Habitación {self.numero} ahora está ocupada.")
        else:
            print(f"Habitación {self.numero} ya está ocupada.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f"Habitación {self.numero} ahora está disponible.")
        else:
            print(f"Habitación {self.numero} ya está libre.")

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero} - {self.tipo} - {estado}"


hotel = []

tipos = ["Individual", "Doble", "Suite"]

for i in range(10):
    tipo = tipos[i % len(tipos)]
    hotel.append(HabitacionHotel(i + 1, tipo))


def mostrar_vacias():
    print("\nHabitaciones disponibles:")
    for h in hotel:
        if not h.ocupada:
            print(h)


def mostrar_ocupadas():
    print("\nHabitaciones ocupadas:")
    for h in hotel:
        if h.ocupada:
            print(h)


def ocupar_habitacion():
    num = int(input("Ingrese número de habitación a ocupar: "))
    if 1 <= num <= len(hotel):
        hotel[num - 1].ocupar()
    else:
        print("Número inválido")


def liberar_habitacion():
    num = int(input("Ingrese número de habitación a liberar: "))
    if 1 <= num <= len(hotel):
        hotel[num - 1].liberar()
    else:
        print("Número inválido")

while True:
    print("\n--- SISTEMA DE HOTEL ---")
    print("1. Mostrar habitaciones vacías")
    print("2. Mostrar habitaciones ocupadas")
    print("3. Ocupar habitación")
    print("4. Liberar habitación")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_vacias()
    elif opcion == "2":
        mostrar_ocupadas()
    elif opcion == "3":
        ocupar_habitacion()
    elif opcion == "4":
        liberar_habitacion()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")