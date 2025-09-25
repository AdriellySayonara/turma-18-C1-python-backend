""" import unittest
from jogo import Guerreiro, Mago, Arqueiro

class TestPersonagens(unittest.TestCase):

    def test_guerreiro_atacar(self):
        g = Guerreiro("Aragorn")
        self.assertEqual(g.atacar(), "Aragorn ataca com espada!")

    def test_mago_atacar(self):
        m = Mago("Gandalf")
        self.assertEqual(m.atacar(), "Gandalf lança uma bola de fogo!")

    def test_arqueiro_atacar(self):
        a = Arqueiro("Legolas")
        self.assertEqual(a.atacar(), "Legolas dispara uma flecha!")

    def test_tomar_dano(self):
        g = Guerreiro("Boromir")
        g.tomar_dano(30)
        self.assertEqual(g.vida, 70)  # Vida deve cair para 70
        g.tomar_dano(100)
        self.assertEqual(g.vida, 0)   # Vida não pode ser negativa

if __name__ == "__main__":
    unittest.main() """


# test_jogo.py
import unittest
from jogo import Guerreiro, Mago, Arqueiro

class TestPersonagens(unittest.TestCase):

    def test_guerreiro_atacar(self):
        g = Guerreiro("Aragorn")
        # ERRO PROPOSITAL: vamos escrever a string errada
        self.assertEqual(g.atacar(), "Aragorn lança uma bola de fogo!")  # Deve falhar

    def test_mago_atacar(self):
        m = Mago("Gandalf")
        self.assertEqual(m.atacar(), "Gandalf lança uma bola de fogo!")  # Certo

    def test_arqueiro_atacar(self):
        a = Arqueiro("Legolas")
        self.assertEqual(a.atacar(), "Legolas dispara uma flecha!")  # Certo

if __name__ == "__main__":
    unittest.main()
