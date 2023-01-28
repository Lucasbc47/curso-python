# Match Case
time = input("Insira seu time favorito de futebol:\n").lower()

match time:
    case 'flamengo' | 'fluminense' | 'vasco' | 'botafogo':
        print('time do rj, tamo junto mané!!!!')
    case 'são paulo' | 'palmeiras' | 'santos' | 'corinthians':
        print('time de sp, tamo junto cachorro!!')
    case _:
        print("pesquisa no google man, sei não")