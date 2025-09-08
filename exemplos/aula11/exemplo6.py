class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_lidas = 0

    def ler(self, qtd_paginas):
        self.paginas_lidas += qtd_paginas
        if self.paginas_lidas > self.paginas:
            self.paginas_lidas = self.paginas
        print(f"Lidas {self.paginas_lidas}/{self.paginas} páginas do livro {self.titulo}")

# Objetos
livro1 = Livro("Python para Iniciantes", "Alyce", 300)
livro1.ler(50)
livro1.ler(300)
