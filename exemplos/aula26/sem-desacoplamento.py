# ==============================
# CÓDIGO SEM DESACOPLAMENTO
# ==============================

class Caminhao:
    def entregar(self):
        return "Entrega feita por caminhão."

class Navio:
    def entregar(self):
        return "Entrega feita por navio."


# Função principal
def planejar_entrega(tipo):
    # Aqui o código depende diretamente das classes concretas
    if tipo == "caminhao":
        transporte = Caminhao()
    elif tipo == "navio":
        transporte = Navio()
    else:
        raise ValueError("Tipo de transporte inválido.")

    return transporte.entregar()


# Uso
print(planejar_entrega("caminhao"))
print(planejar_entrega("navio"))
