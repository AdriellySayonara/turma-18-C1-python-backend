#Herança com super()

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_info(self):
        print(f"Nome: {self.nome}, Salário: {self.salario}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Setor: {self.setor}")

g = Gerente("Alice", 5000, "TI")
g.mostrar_info()

