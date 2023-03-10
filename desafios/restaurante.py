# Desafio Python [1]
# Autor: Lucas Barboza Costa

import os

print(f"""
{'=' * 15}
Menu
{'=' * 15}
Código |  Prato               | Preço 
1      |  Peixe ao molho      | R$: 115,00
2      |  Macarrão com molho  | R$: 33,00
3      |  File mignon         | R$: 65,00
4      |  Frango a parmegiana | R$: 78,00
5      |  Churrasco no prato  | R$: 70,00
""")

option = int(input("Informe o código do prato: "))

if option not in range(1, 5):
    print("Insira um código de prato válido")
    quit()
else:
    print("Obrigado pela preferência!")

gorjetinha_perg = input("Deseja pagar pelo serviço? [s|n]\n>>: ").lower()

if gorjetinha_perg == "s":
    gorjetinha_valor = int(input("[10], [12], [15]\n>>: "))

os.system("cls")
print(f"{'*' * 8} Sua conta {'*' * 8}")

match option:
    case 1:
        prato = "Peixe ao molho"
        price = 115.00
    case 2:
        prato = "Macarrão com molho"
        price = 33.00
    case 3:
        prato = "File mignon"
        price = 65.00
    case 4:
        prato = "Frango a parmegiana"
        price = 78.00
    case 5:
        prato = "Churrasco no prato"
        price = 70.00
    
if gorjetinha_perg == "s":
    final = (price * gorjetinha_valor/100)
    final += price
elif gorjetinha_perg == "n":
    final = price
else:
    final = price

print(f"Prato: {prato} - Valor R$: {final:.2f}")
print("Obrigado pela preferencia!")
