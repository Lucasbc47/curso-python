# Condições 2

n1, n2 = 5, 7
nome = "Orrico"

print(f"""
n1 igual que n2 e n1 maior ou igual que n2:
{n1 == n2 and n1 >= n2}
n1 diferente de n2 ou n1 maior ou igual que n2:
{n1 != n2 or n1 >= n2}
n1 não é igual que n2:
{not n1 == n2}
texto 'rr' se encontra no nome:
{'rr' in nome}
texto 'rr' não se encontra no nome:
{'rr' not in nome}
""")

