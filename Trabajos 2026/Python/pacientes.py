# Clase Paciente
class Paciente:
    def __init__(self, nombre, edad, expediente, diagnostico):
        self.nombre = nombre
        self.edad = edad
        self.expediente = expediente
        self.diagnostico = diagnostico

    def mostrar_datos(self):
        print("\n--- Datos del Paciente ---")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"N° Expediente: {self.expediente}")
        print(f"Diagnóstico: {self.diagnostico}")

    def actualizar_datos(self):
        print("\nActualizar datos del paciente:")
        self.nombre = input("Nuevo nombre: ")
        self.edad = input("Nueva edad: ")
        self.diagnostico = input("Nuevo diagnóstico: ")
        print("Datos actualizados correctamente.")


# Lista para almacenar pacientes
pacientes = []


# Funciones del sistema
def registrar_paciente():
    print("\n--- Registrar Paciente ---")
    nombre = input("Ingrese nombre: ")

    # Validación básica
    while True:
        edad = input("Ingrese edad: ")
        if edad.isdigit():
            edad = int(edad)
            break
        else:
            print("Edad inválida. Intente de nuevo.")

    expediente = input("Ingrese número de expediente: ")

    # Validar que no exista el expediente
    for p in pacientes:
        if p.expediente == expediente:
            print("Ya existe un paciente con ese expediente.")
            return

    diagnostico = input("Ingrese diagnóstico: ")

    nuevo = Paciente(nombre, edad, expediente, diagnostico)
    pacientes.append(nuevo)

    print("Paciente registrado con éxito.")


def mostrar_pacientes():
    print("\n--- Lista de Pacientes ---")
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
    else:
        for p in pacientes:
            p.mostrar_datos()


def buscar_paciente():
    print("\n--- Buscar Paciente ---")
    expediente = input("Ingrese número de expediente: ")

    for p in pacientes:
        if p.expediente == expediente:
            p.mostrar_datos()
            return p

    print("Paciente no encontrado.")
    return None


def actualizar_paciente():
    print("\n--- Actualizar Paciente ---")
    paciente = buscar_paciente()

    if paciente:
        paciente.actualizar_datos()


def eliminar_paciente():
    print("\n--- Eliminar Paciente ---")
    expediente = input("Ingrese número de expediente: ")

    for p in pacientes:
        if p.expediente == expediente:
            pacientes.remove(p)
            print("Paciente eliminado correctamente.")
            return

    print("Paciente no encontrado.")


# Menú principal
def menu():
    while True:
        print("\n===== SISTEMA DE CONTROL DE PACIENTES =====")
        print("1. Registrar paciente")
        print("2. Mostrar pacientes")
        print("3. Buscar paciente")
        print("4. Actualizar paciente")
        print("5. Eliminar paciente")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            mostrar_pacientes()
        elif opcion == "3":
            buscar_paciente()
        elif opcion == "4":
            actualizar_paciente()
        elif opcion == "5":
            eliminar_paciente()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecutar el programa
menu()