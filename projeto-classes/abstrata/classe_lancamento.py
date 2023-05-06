from classe_filmes import *

class Lancamento(Filmes):
    def __init__(self, nome, base):
        Filmes.nome = nome
        Filmes.base = base

    def diaria(self):
        return self.base * 1.25
