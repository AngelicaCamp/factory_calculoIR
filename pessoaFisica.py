from pessoa import Pessoa


class PessoaFisica(Pessoa):

    def __init__(self,nome,idade,cpf,renda_anual):
        self.cpf = cpf
        self.renda_anual = renda_anual
        Pessoa.__init__(self,nome,idade)

   
    def calcularIR(self):
        return self.renda_anual * 0.15

    