class Sensor:
    def __init__(self, id_sensor, tipo, valor):
        self.id_sensor = id_sensor
        self.tipo = tipo
        self.valor = valor

    def obtener_snapshot(self):
        return (self.id_sensor, self.tipo, self.valor)

historial = []

sensor_temperatura = Sensor("SENS-01", "Temperatura", 24.5)
historial.append(sensor_temperatura.obtener_snapshot())

sensor_temperatura.valor = 28.9
historial.append(sensor_temperatura.obtener_snapshot())

print("Historial de Snapshots:")
for snap in historial:
    print(snap) 
    
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = [] 

    def agregar_calificacion(self, nombre_materia, nota, fecha):
        self.calificaciones.append((nombre_materia, nota, fecha))

    def obtener_promedio(self):
        if not self.calificaciones:
            return 0.0

        suma_notas = 0
        
        for materia, nota, fecha in self.calificaciones:
            suma_notas += nota
            
            if nota < 60:
                print(f"¡Alerta! {self.nombre} va dejando {materia} con {nota} (Fecha: {fecha})")
        
        return suma_notas / len(self.calificaciones)

alumno = Estudiante("Panchito")
alumno.agregar_calificacion("Programación I", 85, "2026-04-15")
alumno.agregar_calificacion("Bases de Datos", 55, "2026-05-10") 
alumno.agregar_calificacion("Matemáticas", 70, "2026-05-20")

promedio_final = alumno.obtener_promedio()
print(f"Promedio general de {alumno.nombre}: {promedio_final:.2f}")

import datetime

class SistemaAuditoria:
    def __init__(self):
        self.log_auditoria = [] # Lista de tuplas

    def registrar_acceso(self, id_transaccion, usuario, monto):
        # Generamos el timestamp en el momento exacto
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Guardamos el registro como una tupla inmutable
        registro = (id_transaccion, usuario, monto, timestamp)
        self.log_auditoria.append(registro)
        print(f"Auditoría guardada con éxito para la transacción: {id_transaccion}")


class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def realizar_retiro(self, usuario, monto, auditor, id_tx):
        if monto <= self.saldo:
            self.saldo -= monto
            auditor.registrar_acceso(id_tx, usuario, monto)
            return f"Retiro exitoso. Nuevo saldo: ${self.saldo}"
        return "Saldo insuficiente."
    
banco_auditor = SistemaAuditoria()
cuenta_vip = CuentaBancaria("CTA-9990", 5000.0)

print(cuenta_vip.realizar_retiro("Carlos_Mendoza", 1200.0, banco_auditor, "TX-10024"))

print("\n--- REGISTROS EN LA BÓVEDA DE AUDITORÍA ---")
print(banco_auditor.log_auditoria)