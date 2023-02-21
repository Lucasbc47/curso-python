# Funções
def ola(nome:  str):    
    print(f"olá, {nome}")

def numeros(pnum: int, snum: int):
    print(f"Primeiro número: {pnum}\nSegundo número: {snum}\nSoma: {pnum+snum}")

def variacao(arg, *sla):
    print(f"Primeiro argumento: {arg}")
    
    for item in sla:
        print(item)
    return

ola('Lucas')
numeros(39, 28)
variacao("sla", "doido")