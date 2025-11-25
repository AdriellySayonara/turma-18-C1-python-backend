class Usuario:
     def __init__(self, nome):
          self.nome = nome
     def receber_nototificacao(self, titulo):
          print(f"{self.nome} recebeu notificação: {titulo}")
          
class Canal:
     def __init__(self, nome):
          self.nome = nome
          self.usuario1 = Usuario('Ana')
          self.usuario2 = Usuario('Pedro')
     
     def novo_video(self, titulo):
          print(f'Canal {self.nome} publicou: {titulo}')
          self.usuario1.receber_nototificacao(titulo)
          self.usuario2.receber_nototificacao(titulo)

if __name__ == "__main__":
     canal = Canal('Canal Como')
     canal.novo_video("Como as abelhas polinizam")
     
#jeito correto do observer 

from abc import ABC, abstractmethod

class Observador(ABC): #interface do observador
     @abstractmethod
     def atualizar(self, titulo: str):
          pass

class Sujeito(ABC): #interface do sujeito
     @abstractmethod
     def adicionar(self, observador: Observador):
          pass

class Sujeito(ABC): #interface do sujeito
     @abstractmethod
     def remover(self, observador: Observador):
          pass
     
class Sujeito(ABC): #interface do sujeito
     @abstractmethod
     def remover(self, titulo: str):
          pass

class Canal(Sujeito):
     def __init__(self):
          self._observadores = []
     
     def adicionar(self, observador):
          self._observadores.append(observador)
     
     def remover(self, observador):
          self._observadores.remove(observador)
     
     def notificar(self, titulo):
          for observador in self._observadores:
               observador.atualizar(titulo)
     
     def novo_video(self, titulo):
          print(f'Novo video publicado: {titulo}')
          self.notificar(titulo)
          
class Usuario(Observador):
     def __init__(self, nome):
          self.nome = nome
     
     def atualizar(self, titulo):
          print(f'{self.nome} foi notificado so novo vídeo do canal: {titulo}')
     
     if __name__ == "__main__":
          canal = Canal()
          
          