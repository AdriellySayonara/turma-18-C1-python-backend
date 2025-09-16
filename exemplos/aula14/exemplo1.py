#herança simples
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def som(self):
        print("Som genérico de animal")

class Cachorro(Animal):
    def som(self):
        print("Au Au!")

class Gato(Animal):
    def som(self):
        print("Miau!")

#objeto
c1 = Cachorro("Rex")
c2 = Gato("Mimi")

#c1.som()
#c2.som()


#polimorfismo em ação
def emitir_som(animal):
    animal.som()

animais = [Cachorro("Rex"), Gato("Mimi"), Animal("Genérico")]

for a in animais:
    emitir_som(a)
    
    