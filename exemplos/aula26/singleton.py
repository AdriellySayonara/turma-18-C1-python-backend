class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Criando nova instância Singleton...")
            cls._instancia = super().__new__(cls)
        return cls._instancia

# Teste
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True
