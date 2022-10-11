from enum import Enum


class Pessoa:

    # método construtor
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
        
class TipoPessoa(Enum):
    PESSOA_FISICA = 1
    PESSOA_JURIDICA = 2 


