# Carlos David Pravia Herrera y Angel Ramon Gavarria Munguia

class Empleado:
    def __init__(self, nombre, id_empleado, año_ingreso):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.año_ingreso = año_ingreso
        self.año_actual = 2026

    def años_en_empresa(self):
        return self.año_actual - self.año_ingreso

    def mostrar_datos(self):
        años = self.años_en_empresa()
        print(f"Nombre: {self.nombre} | ID: {self.id_empleado} | Años en empresa: {años}")

    def calcular_salario(self):
        return 0

class Asalariado(Empleado):
    def __init__(self, nombre, id_empleado, año_ingreso, salario_base):
        super().__init__(nombre, id_empleado, año_ingreso)
        self.salario_base = salario_base

    def calcular_salario(self):
        salario = self.salario_base
        if self.años_en_empresa() > 5:
            salario += 100
        return salario

class PorHoras(Empleado):
    def __init__(self, nombre, id_empleado, año_ingreso, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, id_empleado, año_ingreso)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        if self.horas_trabajadas > 160:
            extras = self.horas_trabajadas - 160
            salario = (160 * self.pago_por_hora) + (extras * self.pago_por_hora * 2)
        else:
            salario = self.horas_trabajadas * self.pago_por_hora
        
        if self.años_en_empresa() > 3:
            salario += 50
            
        return salario

class Comisionista(Empleado):
    def __init__(self, nombre, id_empleado, año_ingreso, ventas_del_mes, porcentaje_comision):
        super().__init__(nombre, id_empleado, año_ingreso)
        self.ventas_del_mes = ventas_del_mes
        self.porcentaje_comision = porcentaje_comision

    def calcular_salario(self):
        salario = self.ventas_del_mes * self.porcentaje_comision
        
        if self.ventas_del_mes > 10000:
            salario += 200
            
        if self.años_en_empresa() < 2:
            salario -= 50
            
        return salario

def generar_planilla(empleados):
    print("Planilla")
    total_empresa = 0
    
    for emp in empleados:
        emp.mostrar_datos()
        salario_final = emp.calcular_salario() 
        print(f"Salario a pagar: ${salario_final:,.2f}")
        print("-" * 40)
        total_empresa += salario_final
        
    print(f"Total a pagar: ${total_empresa:,.2f}")

emp1 = Asalariado("Ana Gómez", "E001", 2018, 2500)
emp2 = PorHoras("Luis Pérez", "E002", 2022, 180, 12)
emp3 = Comisionista("Marta Ríos", "E003", 2024, 12000, 0.08)

generar_planilla([emp1, emp2, emp3])