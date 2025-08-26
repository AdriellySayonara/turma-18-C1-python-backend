#pedir ao usuário para digitar as notas de 5 alunos e calcular a média de cada um


for i in range(1, 6): # de 1 a 5
     
     soma = 0
     
     for j in range(1, 4): # de 1 a 3
          nota = float(input(f'Digite a nota {j} do aluno {i}: '))
          soma += nota
     
     media = soma / 3
     
     print(f'A média do aluno {i} é: {media}') #9.575269158
     print(f'A média do aluno {i} é: {media:.4f}') #9.58
     
     
     
