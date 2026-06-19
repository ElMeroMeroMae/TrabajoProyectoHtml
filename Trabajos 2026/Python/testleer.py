import mysql.connector
import csv  

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_password",
    database="universidad"
)
cursor = conexion.cursor()

def crear_estudiante():
    print("\n--- Registrar Nuevo Estudiante ---")
    nombre = input("Ingrese nombre: ")
    carrera = input("Ingrese carrera: ")

    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if edad < 0:
                print("¡Error de máquina! La edad no puede ser negativa. Intente de nuevo.")
            elif edad > 120:
                print("Ideay, ¿un estudiante de más de 120 años? Ingrese una edad válida.")
            else:
                break  
        except ValueError:
            print("Por favor, ingrese un número entero válido para la edad.")

    sql = "INSERT INTO estudiantes (nombre, carrera, edad) VALUES (%s, %s, %s)"
    valores = (nombre, carrera, edad)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Estudiante agregado correctamente.\n")


def leer_estudiantes():
    cursor.execute("SELECT * FROM estudiantes")
    resultados = cursor.fetchall()
    print("\nLista de estudiantes:")
    for fila in resultados:
        print(fila)
    print()


def actualizar_estudiante():
    id = int(input("Ingrese ID del estudiante a actualizar: "))
    nuevo_nombre = input("Nuevo nombre: ")
    nueva_carrera = input("Nueva carrera: ")
    
    while True:
        nueva_edad = int(input("Nueva edad: "))
        if nueva_edad >= 0:
            break
        print("La edad no puede ser negativa.")
        
    sql = "UPDATE estudiantes SET nombre=%s, carrera=%s, edad=%s WHERE id=%s"
    valores = (nuevo_nombre, nueva_carrera, nueva_edad, id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Estudiante actualizado correctamente.\n")


def eliminar_estudiante():
    id = int(input("Ingrese ID del estudiante a eliminar: "))
    sql = "DELETE FROM estudiantes WHERE id=%s"
    valores = (id,)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Estudiante eliminado correctamente.\n")

def buscar_por_carrera():
    print("\n--- Buscar Estudiantes por Carrera ---")
    carrera_buscar = input("Ingrese el nombre de la carrera que desea buscar: ")
    
    sql = "SELECT * FROM estudiantes WHERE carrera = %s"
    cursor.execute(sql, (carrera_buscar,))
    resultados = cursor.fetchall()
    
    if resultados:
        print(f"\nEstudiantes encontrados en la carrera '{carrera_buscar}':")
        for fila in resultados:
            print(f"ID: {fila[0]} | Nombre: {fila[1]} | Edad: {fila[3]}")
    else:
        print(f"No se encontraron alumnos matriculados en '{carrera_buscar}'.")
    print()

def contar_registros():
    sql = "SELECT COUNT(*) FROM estudiantes"
    cursor.execute(sql)
    total = cursor.fetchone()[0]
    print(f"\n[INFO]: Actualmente hay un total de {total} estudiantes registrados en la tabla.\n")

def exportar_resultados():
    print("\nExportar Expedientes")
    cursor.execute("SELECT * FROM estudiantes")
    resultados = cursor.fetchall()
    
    if not resultados:
        print("No hay datos en la base de datos para exportar.\n")
        return

    nombre_archivo = "reporte_estudiantes.csv"
    
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID", "Nombre", "Carrera", "Edad"])
        escritor.writerows(resultados)
        
    print(f"¡Pum! Datos exportados con éxito en el archivo: '{nombre_archivo}'.\n")

def menu():
    while True:
        print("--- MENÚ CRUD ESTUDIANTES (VERSION PREMIUM) ---")
        print("1. Crear estudiante")
        print("2. Leer estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Buscar por carrera (Actividad 2)")
        print("6. Contar total de registros (Actividad 3)")
        print("7. Exportar datos a CSV (Actividad 4)")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_estudiante()
        elif opcion == "2":
            leer_estudiantes()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            buscar_por_carrera()
        elif opcion == "6":
            contar_registros()
        elif opcion == "7":
            exportar_resultados()
        elif opcion == "8":
            print("Saliendo del programa... ¡Nos vemos, primo!")
            break
        else:
            print("Opción inválida, intente de nuevo.\n")

menu()

cursor.close()
conexion.close()