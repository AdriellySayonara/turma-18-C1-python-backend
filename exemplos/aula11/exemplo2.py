class Escola:  # a receita
    def __init__(self, nome, qtd_alunos):
        self.nome = nome
        self.qtd_alunos = qtd_alunos

    def apresentar(self): #método
        print(f"{self.nome} tem {self.qtd_alunos} alunos.")

# criando bolos (objetos)
escola1 = Escola("Escola A", 500)
escola2 = Escola("Escola B", 300)

escola1.apresentar()  # Escola A tem 500 alunos.
escola2.apresentar()  # Escola B tem 300 alunos.
