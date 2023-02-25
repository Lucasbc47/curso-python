# Heranças
from classes_heranca import PessoaAutenticavel

p = PessoaAutenticavel(
    nome="Lucas",
    sobrenome="Barboza Costa",
    sexo="M",
    idade=17,

    cpf="123-456-789-00",
    ativo=True,

    usuario="lucasbc",
    senha="1234567lucas"    
)

p.autenticar(usuario="lucasbc", senha="1234lucas")
