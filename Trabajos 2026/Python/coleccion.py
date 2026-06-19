class Libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

class Biblioteca:
    def __init__(self):
        self.libros = []        
        self.indice = {}        

    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.indice[libro.codigo] = libro

    def buscar(self, codigo):
        return self.indice.get(codigo, "Libro no encontrado")

    def prestar(self, codigo):
        libro = self.indice.get(codigo)
        if libro and libro.disponible:
            libro.disponible = False
            return f"Prestaste: {libro.titulo}"
        return "No disponible o no existe"

    def devolver(self, codigo):
        if codigo in self.indice:
            self.indice[codigo].disponible = True
            return "Libro devuelto"

    def mostrar_disponibles(self):
        return [l.titulo for l in self.libros if l.disponible]

    def contar_total(self):
        return len(self.libros)

repo = Biblioteca()
repo.agregar_libro(Libro("L01", "Cien Años de Soledad", "Gabo"))
print(f"Disponibles: {repo.mostrar_disponibles()}")