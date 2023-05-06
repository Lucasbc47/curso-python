# Classes, OOP
class ClassOne:
    """
    t = ClassOne()
    print(t.soma(x=10, y=10))
    """    
    def __init__(self):
        pass

    def soma(self, x: int, y: int):
        return x + y
    
class Pessoax:
    def __init__(self, nome: str, sobrenome: str, sexo: str, 
        cpf: str, ativo: bool, usuario: str, senha: str, idade: int):
        
        self.nome = nome
        self.sobrenome = sobrenome
        self.usuario = usuario

        self.senha = senha
        self.sexo = sexo
        self.idade = idade
        
        self.cpf = cpf
        self.ativo = ativo

    def full_name(self):
        return f"{self.nome} {self.sobrenome}"

    def disable(self):
        self.ativo = False
    
    def activate(self):
        self.ativo = True

class PessoaAutenticavel(Pessoax):
    def __init__(self, nome: str, sobrenome: str, sexo: str, cpf: str, ativo: bool, usuario: str, senha: str, idade: int):
        super().__init__(nome, sobrenome, sexo, cpf, ativo, usuario, senha, idade)
    
    def autenticar(self, usuario, senha):
        
        if self.usuario == usuario and self.senha == senha:
            return True
        else:
            return False

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, cpf: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

class Cliente(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cpf: str, matricula: str):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
    
    def indentificacao(self):
        return self.__matricula

class Funcionario(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cpf: str, matricula: str):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
    
    def indentificacao(self):
        return self.__matricula

cliente = Cliente(nome='Lucas', sobrenome='Barboza', cpf='123.456.789-01', matricula='201')
funcionario = Funcionario(nome='Lucas', sobrenome='Barboza', cpf='123.456.789-01', matricula='202')


print(f"Cliente: {cliente.nome_completo()}\nID: {cliente.indentificacao()}")
print(f"Funcionário: {funcionario.nome_completo()}\nID: {funcionario.indentificacao()}")