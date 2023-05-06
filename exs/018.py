# Funções 4
def calcularPagamento(valor: float, dias: int):
    
    multa = 0.03
    multa_dia = 0.001 * dias

    if dias < 1:
        multa_dia = 0
        multa = 0

    diario = []
    diario.append(valor + (valor * multa_dia) + (valor * multa))
    return diario

    
while True:

    valor_prestacao = float(input("Digite valor da prestação:\n"))
    dias_atrasado = int(input("Dias atrasados:\n"))
    
    valor_a_pagar = calcularPagamento(valor_prestacao, dias_atrasado)

    print(f"O valor a ser pago R$: {valor_a_pagar}")
    continuar = input("Digite [s|n] para continuar:\n").lower()

    if continuar == "n":
        break
    