import datetime

class Logger:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._log = []  # inicializa o log
        return cls._instancia

    def registrar(self, mensagem):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._log.append(f"[{timestamp}] {mensagem}")

    def exibir_logs(self):
        for linha in self._log:
            print(linha)

# Uso
logger1 = Logger()
logger2 = Logger()

logger1.registrar("Sistema iniciado")
logger2.registrar("Usuário autenticado")

logger1.exibir_logs()
print("Mesma instância?", logger1 is logger2)  # True