# assert_methods.py
"""
Lista de métodos de assert disponíveis em unittest.TestCase

Esses métodos são usados dentro de classes que herdam de TestCase para verificar comportamentos.
"""

# Comparação de igualdade
assertEqual(a, b)           # Testa se a == b
assertNotEqual(a, b)        # Testa se a != b

# Verdadeiro / Falso
assertTrue(x)               # Testa se x é True
assertFalse(x)              # Testa se x é False

# Inclusão / pertencer a algo
assertIn(a, b)              # Testa se a está contido em b
assertNotIn(a, b)           # Testa se a NÃO está contido em b

# Tipos e instâncias
assertIs(a, b)              # Testa se a é b (mesmo objeto)
assertIsNot(a, b)           # Testa se a NÃO é b
assertIsNone(x)             # Testa se x é None
assertIsNotNone(x)          # Testa se x NÃO é None
assertIsInstance(a, b)      # Testa se a é instância da classe b
assertNotIsInstance(a, b)   # Testa se a NÃO é instância da classe b

# Lançamento de exceções
assertRaises(exc, fun, *args, **kwargs)  # Testa se a função lança a exceção esperada
assertRaisesRegex(exc, regex, fun, *args, **kwargs)  # Testa se lança exceção e mensagem corresponde ao regex

# Comparação numérica
assertAlmostEqual(a, b)     # Testa se a ~= b (aproximadamente igual)
assertNotAlmostEqual(a, b)  # Testa se a NÃO é aproximadamente igual a b

# Comparação de sequência
assertCountEqual(a, b)      # Testa se duas sequências têm os mesmos elementos, sem ordem
