valor = 10
if valor:
     print("O valor é diferente de zero => verdade. ")
valor = 0
if not valor:
     print("O valor é falso, mas o not inverteu o valor.")
     
zero_interio = 0 # -> False
zero_float = 0.0 # -> False
none = None # -> False
string_vazia = "       " # -> False
colecoes_vazias = [] #{}, set(), tuple() -> False
qualquer_outro_valor = "-1" # -> True


print(bool(zero_interio))  # False
print(bool(zero_float))   # False
print(bool(none))         # False 
print(bool(string_vazia))  # False
print(bool(colecoes_vazias))  # False
print(bool(qualquer_outro_valor))  # True

