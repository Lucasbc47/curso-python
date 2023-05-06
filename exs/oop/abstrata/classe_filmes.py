from abc import ABC, abstractclassmethod

class Filmes(ABC):
    nome = None
    base = None

    @abstractclassmethod
    def diaria(self):
        pass
    