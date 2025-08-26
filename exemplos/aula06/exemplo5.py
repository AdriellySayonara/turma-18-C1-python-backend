""" # interando listas com for
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]

for i in cidades:
     print("Cidade:", i )
      
       """
       
#interando listas com indice
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
for i in range(len(cidades)):
    print(f"Cidade {i + 1}: {cidades[i]}")
    
#usando enumerate
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
for indice, i in enumerate(cidades):
    print(f"Cidade {indice + 1}: {i}")
