import os

meses = [i for i in range(0, 11)]
valMes = [0]*11
valAno = 0
valSer = 0

while True:
    print(f"""
[1] Informar um novo serviço
[2] Exibir relatório
[3] Sair
""")
    op = int(input("Insira uma opção:\n"))
    
    match op:
        case 1:
            valSer = int(input("Insira o valor recebido do serviço:\n"))
            mes =  int(input("Insira o número do mês que foi recebido:\n"))
            valMes[mes-1] = valSer + valMes[mes-1]
            valAno = valAno + valSer
            os.system("cls")
        case 2:
            print(" -- Meses --")
            for i in range(0, 12):
                print(f"Mês: [{i+1}] || R$: {valMes[i-1]}")

            print(" -- Ano --")
            print(f"Total R$: {valAno}")
            print(" ----------")
            input("Digite qualquer tecla para continuar...")
            os.system("cls")
        case 3:
            print("Até a próxima!")
            break
        case _:
            print("Insira uma opção válida!")
            input("Digite qualquer tecla para continuar...")
            os.system('cls')

