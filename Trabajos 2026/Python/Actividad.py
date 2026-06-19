class VehiculoPeaje:
    tarifas={
        "Auto":100,
        "Camion":300,
        "Moto":50
    }
    def __init__(self, patente, tipo, saldo_inicial): 
        self.patente=patente
        if tipo in self.tarifas:
            self.tipo=tipo
        else:
            self.tipo="Auto"
        self.saldo_inicial=saldo_inicial
        0