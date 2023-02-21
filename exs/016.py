# Funções 2
def imprimeLinha(numero):
    for n in range(1, numero+1):
        print(n, end="")
    print() 

def imprimeSequencia(numero):
    for numero in range(numero + 1):
        imprimeLinha(numero)

numero = int(input("Insira um número:\n"))
imprimeSequencia(numero)