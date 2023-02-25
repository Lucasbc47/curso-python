from classe_filmes import *

class Comum(Filmes):
    def __init__(self, nome, base):
        Filmes.nome = nome
        Filmes.base = base
    
    def diaria(self):
        return self.base