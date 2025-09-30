def calculadora_segura(num1, num2, operador):
    try:
        # Tentar realizar a operação
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2
        else:
            print("Erro: Operador inválido. Use +, -, *, ou /.")
            return # Sair da função se o operador for inválido

        print(f"O resultado de {num1} {operador} {num2} é: {resultado}")

    except ZeroDivisionError:
        # Lidar com a divisão por zero
        print("Erro: Não se pode dividir por zero.")
    except TypeError:
        # Lidar com entrada que não é um número
        print("Erro: Verifique se os parâmetros são números válidos.")

# Exemplos de uso
calculadora_segura(10, 5, '+')
calculadora_segura(10, 0, '/')
calculadora_segura(10, "5", '*')