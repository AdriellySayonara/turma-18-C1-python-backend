#imposto com função

def calcular_imposto(salario):
    if salario <= 1903.98:
        return 0
    elif salario <= 2826.65:
        return salario * 0.075
    elif salario <= 3751.05:
        return salario * 0.15
    elif salario <= 4664.68:
        return salario * 0.225
    else:
        return salario * 0.275 
      
salario = float(input("Digite o salário: "))
imposto = calcular_imposto(salario)
print(f"O imposto devido é: R$ {imposto:.2f}")