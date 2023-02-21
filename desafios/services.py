# Desafio Python [2]
# Autor: Lucas Barboza Costa
import os

os.system('cls' if os.name == 'nt' else 'clear')

meses = [i for i in range(0, 12)]
valMes = [0]*12
valAno = 0
valSer = 0

while True:
    print(f"""
[1] Informar um novo serviço
[2] Exibir relatório
[3] Sair
""")
    try:
        op = int(input("Insira uma opção:\n"))
    except:
        print("Insira uma opção válida!")
        input("Digite qualquer tecla para continuar...")
        break

    match op:
        case 1:
            try:
                valSer = float(input("Insira o valor recebido do serviço:\n"))                
                mes =  int(input("Insira o número do mês que foi recebido:\n"))

                if mes not in range(1, 13):
                    print("Mês tem que estar entre 1 e 12.")
                    input("Digite qualquer tecla para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')

                    continue

            except:
                print("- Troque [,] por [.] se possivel")
                print("- Verifique se você inseriu números")
                input("Digite qualquer tecla para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

                continue
            
            valMes[mes-1] = valSer + valMes[mes-1]
            valAno = valAno + valSer
            os.system('cls' if os.name == 'nt' else 'clear')


        case 2:
            os.system('cls' if os.name == 'nt' else 'clear')

            print("---- Meses ----")
            for i in range(0, 12):
                print(f"Mês: [{i+1}] || R$: {valMes[i]}")
            print("--------")

            print("---- Ano ----")
            print(f"Total R$: {valAno:.2f}")
            print(" ----------")

            input("Digite enter para continuar...") 
            os.system('cls' if os.name == 'nt' else 'clear')


        case 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Até a próxima!")
            break
        case _:
            print("Insira uma opção válida!")
            input("Digite qualquer tecla para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

            

