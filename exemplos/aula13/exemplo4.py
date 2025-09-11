from abc import ABC, abstractmethod

# Classe abstrata
class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

dog = Cachorro()
cat = Gato()

print(dog.emitir_som())  # Au au!
print(cat.emitir_som())  # Miau!
