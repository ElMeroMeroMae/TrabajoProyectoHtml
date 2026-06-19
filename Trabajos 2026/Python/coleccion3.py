class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

class Inventario:
    def __init__(self):
        self.productos = []
        self.categorias = {} 

    def agregar(self, p):
        self.productos.append(p)
        if p.categoria not in self.categorias:
            self.categorias[p.categoria] = []
        self.categorias[p.categoria].append(p)

    def valor_total(self):
        return sum(p.precio * p.stock for p in self.productos)

    def agotados(self):
        return [p.nombre for p in self.productos if p.stock == 0]

    def eliminar(self, codigo):
        self.productos = [p for p in self.productos if p.codigo != codigo]

    def reporte_ordenado(self):
        ordenados = sorted(self.productos, key=lambda x: x.precio)
        return [(p.nombre, p.precio) for p in ordenados]

inv = Inventario()
inv.agregar(Producto("P01", "Mouse", "Tech", 25.0, 10))
print(f"Valor total: ${inv.valor_total()}")