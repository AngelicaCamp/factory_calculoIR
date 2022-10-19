from pessoa import Pessoa
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica
from pessoa import TipoPessoa


class PessoaFactory:
    
    @staticmethod
    def create(tipo: TipoPessoa, renda_anual) -> Pessoa:
        if tipo == TipoPessoa.PESSOA_FISICA:
            return PessoaFisica('Maria',30,'123.456.789-10',renda_anual)
        
        if tipo == TipoPessoa.PESSOA_JURIDICA:
            return PessoaJuridica('Nubank',9,'123.456.0001/78',renda_anual)
        
        return None

    
if __name__ == '__main__':
    pf = PessoaFactory.create(TipoPessoa.PESSOA_FISICA,36000)
    pj = PessoaFactory.create(TipoPessoa.PESSOA_JURIDICA,100000)

    print(f'Valor a pagar de IR - Pessoa Física: R${pf.calcularIR():.2f}')
    print(f'Valor a pagar de IR - Pessoa Jurídica: R${pj.calcularIR():.2f}')