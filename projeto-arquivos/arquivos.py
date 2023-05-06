import shutil
import os

class Arquivos:

    __author__ = "Lucasbc"

    def copy(origem: str, destino: str):
        for filename in os.listdir(origem):
            if filename.endswith(".jpg"):
                shutil.copy(os.path.join(origem, filename), os.path.join(destino, filename))
        
    def move(origem: str, destino: str):
        for filename in os.listdir(origem):
            if filename.endswith(".jpeg"):
                shutil.move(os.path.join(origem, filename), os.path.join(destino, filename))
    
    def delete(origem: str):
        for filename in os.listdir(origem):
            if filename.endswith(".jpeg"):
                os.remove(os.path.join(origem, filename))

    def criar(filename: str, tipo: str):
        return open(filename, tipo)
    
    def escrever(filename: str, text: list):
        with open(f"{filename}.txt", "a+") as f:
            for t in text:
                f.writelines(f"{t}\n")
    
    def leitura(filename: str):
        with open(f"{filename}.txt", "r") as f:
            text = f.readlines()
        print(text)

    


Arquivos.escrever("teste", ["abc", "def"])
Arquivos.leitura("teste")