class Carro:
    def __init__(self, marca, modelo, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = combustivel

    def abastecer(self, litros):
        self.combustivel += litros
        print(f"Abastecidos {litros}L. Total: {self.combustivel}L")

    def dirigir(self, km):
        gasto = km * 0.1  # exemplo simplificado
        if gasto <= self.combustivel:
            self.combustivel -= gasto
            print(f"Dirigiu {km} km. Combustível restante: {self.combustivel}L")
        else:
            print("Combustível insuficiente!")

# Objetos
carro1 = Carro("Fiat", "Uno", 10)
carro2 = Carro("Ford", "Ka", 5)

carro1.abastecer(20)
carro1.dirigir(30)

carro2.abastecer(20)
carro2.dirigir(30)

