class Tarea: 
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada=False
        
mis_tareas= [Tarea("Hacer la compra"), Tarea("Limpiar la casa"), Tarea("Estudiar para el examen")]

for tarea in mis_tareas:
    tarea.completada=True
    print(f"Tarea: {tarea.descripcion}, Completada: {tarea.completada}")
    
class Producto:
    def __init__(self, sku, nombre):
        self.sku=sku 
        self.nombre=nombre
        
p1= Producto("001", "Camiseta")
p2= Producto("002", "Pantalón")

inventario= {p1.sku: p1, p2.sku: p2}

def buscar_producto(sku):
    resultado = inventario.get(sku, "Error: Producto no encontrado")
    return resultado

print (buscar_producto("001"))
print (buscar_producto("002"))
print (buscar_producto("Z990"))

invitados_bruto=["Ana", "Beto", "Ana", "Carlos", "Beto", "Diana", "Ana"]
invitados_unicos= set(invitados_bruto)
print(invitados_unicos)
print(f"Cantidad de invitados únicos: {len(invitados_unicos)}")