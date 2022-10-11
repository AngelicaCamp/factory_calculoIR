from pessoa import Pessoa
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica
from pessoa import TipoPessoa


class PessoaFactory:
    
    @staticmethod
    def create(tipo: TipoPessoa) -> Pessoa:
        if tipo == TipoPessoa.PESSOA_FISICA:
            return PessoaFisica('Maria',30,'123.456.789-10',36000)
        
        if tipo == TipoPessoa.PESSOA_JURIDICA:
            return PessoaJuridica('Nubank',9,'123.456.0001/78',100000)
        
        return None

    
if __name__ == '__main__':
    pf = PessoaFactory.create(TipoPessoa.PESSOA_FISICA)
    pj = PessoaFactory.create(TipoPessoa.PESSOA_JURIDICA)

    print(f'Valor a pagar de IR - Pessoa Física: R${pf.calcularIR():.2f}')
    print(f'Valor a pagar de IR - Pessoa Jurídica: R${pj.calcularIR():.2f}')