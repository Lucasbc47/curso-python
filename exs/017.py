# Funções 3
def hora(horas, minutos):

    hora_corrigida = horas / 12

    if hora_corrigida <= 1:
        hh = str(horas)
        print(f"Sua hora: {hh}:", end="")
    elif hora_corrigida > 1 and hora_corrigida < 2:
        hhh = str(horas-12)
        print(f"Sua hora: {hhh}:", end="")
    else:
        print("Insira um formato de hora valido.")
    
    if hora_corrigida <= 1 and minutos <= 60:
        print(f"{minutos} a.m")
    elif hora_corrigida > 1 and minutos <= 60:
        print(f"{minutos} p.m")
    else: 
        print("Insira um formato de minutos valido.")
        

hour = int(input("Digite a hora:\n"))
minutes = int(input("Digite os minutos:\n"))
hora(hour, minutes)
