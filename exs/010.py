valor = float(input("Mercadoria:"))
op = int(input("digite 1 para parcelar ou 2 pagamento a vista"))

match op:
    case 1:
        if valor > 1000:
            parcelas = valor/5 
            print(f'Com esse valor você pode parcelar em 5x de R$: {parcelas}')
        else:
            parcelas = valor/3
            print(f'pode parcelar em 3x de r$: {parcelas}')
        
    case 2:
        avista = (valor * 0.9)
        print(f"a vista:  {avista}")

    case _:
        print("invalido")