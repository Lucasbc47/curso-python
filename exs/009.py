# Match Case
time = input("Insira seu time favorito de futebol:\n").lower()

match time:
    case 'flamengo' | 'fluminense' | 'vasco' | 'botafogo':
        print('Time carioca')
    case 'são paulo' | 'palmeiras' | 'santos' | 'corinthians':
        print('Time paulista')
    case _:
        print("Deve ser de outro estado")    