from pessoa import Pessoa


class PessoaJuridica(Pessoa):

    def __init__(self, nome,idade,cnpj,renda_anual):
        self.cnpj = cnpj
        self.renda_anual = renda_anual
        Pessoa.__init__(self,nome,idade)


    def calcularIR(self):
        return self.renda_anual * 0.25

    