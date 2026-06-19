from abc import ABC, abstractmethod

class DocumentoFiscal(ABC):
    def __init__(self, negocio):
        self.negocio=negocio

    @abstractmethod
    def impirmir(self):
        pass

class Recibo(DocumentoFiscal):
    def __init__(self, negocio, monto):
        super().__init__(negocio)
        self.monto=float(monto)

    def impirmir(self):
        print(f"Recibo del negocio {self.negocio} por un monto de {self.monto}")

class Factura(DocumentoFiscal):
    def __init__(self, negocio, total):
        super().__init__(negocio)
        self.total=float(total)

    def impirmir(self):
        print(f"Factura del negocio {self.negocio} por un total de {self.total}")
documentos=[
    Recibo("Mercado", 150.70),
    Factura("Pulperia", 250.25)
]

for doc in documentos:
    doc.impirmir()