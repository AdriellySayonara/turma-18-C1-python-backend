def divisao_segura():
    try:
        # A parte "sensível" do código, onde o erro pode ocorrer.
        dividendo = float(input("Digite o dividendo: "))
        divisor = float(input("Digite o divisor: "))

        # Tentar fazer a divisão. Se o divisor for 0, o erro acontece aqui.
        resultado = dividendo / divisor

    # O 'except' captura especificamente o erro de divisão por zero.
    except ZeroDivisionError:
        print("Erro: Não se pode dividir por zero!")

    # O 'except' também pode capturar outros erros, como o de valor.
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

    # Se a divisão for bem-sucedida, este bloco é executado.
    else:
        print(f"O resultado da divisão é: {resultado}")

# Chamamos a função para testar o comportamento.
divisao_segura()