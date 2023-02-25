from classe_comum import Comum
from classe_infantil import Infantil
from classe_lancamento import Lancamento

l = Lancamento('CREED 3', 10)
print(f"Diaria R$: {l.diaria():.2f}")

c = Comum('Avatar 2', 7)
print(f"Diaria R$: {c.diaria():.2f}")

i = Infantil('Patas em Furia', 5)
print(f"Diaria R$: {i.diaria():.2f}") 