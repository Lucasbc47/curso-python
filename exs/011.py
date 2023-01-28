def menu():
    print(f"""
{'=' * 15}
Criança esperança
{'=' * 15}
Obrigado por ajudar!

[1] Doar R$10
[2] Doar R$25
[3] Doar R$50
[4] Para doar outros valores
[5] Sair
    """)
    
    option = int(input("Insira uma opção:\n"))

    match option:
        case 1:
            valor = 10
        case 2: 
            valor = 25
        case 3:
            valor = 50
        case 4:
            valor = int(input("Insira o valor da doação\nR$: "))
        case 5:
            print('Que pena, me doa na proxima.')
        
    print(f"{'=' * 10}")
    print(f"Você doou R$ {valor}, obrigado.")
    print(f"{'=' * 10}")

if __name__ == "__main__":
    menu()