# mais ifs
while True:

    sexo = input("Insira seu sexo correspondente [m|f]:\n").lower()

    if sexo not in ['m', 'f']:
        # se o sexo não estiver entre m e f
        print('Insira o sexo correto')
    
    elif sexo in ['m', 'f']:
        # se estiver
        print('Sexo validado')
        break
        # passou

    else:
        print("Sexo invalido")
        break