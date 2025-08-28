#imposto sem função

salario = float(input("Digite o salário: ")) 
if salario <= 1903.98:
    imposto = 0 
elif salario <= 2826.65:
    imposto = salario * 0.075
elif salario <= 3751.05:
    imposto = salario * 0.15
elif salario <= 4664.68:
     imposto = salario * 0.225
else:
     imposto = salario * 0.275
print(f"O imposto devido é: R$ {imposto:.2f}")
