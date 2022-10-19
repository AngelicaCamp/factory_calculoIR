from pessoa import Pessoa
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica
from pessoa import TipoPessoa


class PessoaFactory:
    
    @staticmethod
    def create(tipo: TipoPessoa, nome,idade,renda_anual) -> Pessoa:
        if tipo == TipoPessoa.PESSOA_FISICA:
            return PessoaFisica(nome,idade,renda_anual)
        
        if tipo == TipoPessoa.PESSOA_JURIDICA:
            return PessoaJuridica(nome,idade,renda_anual)
        
        return None

    
if __name__ == '__main__':
    pf = PessoaFactory.create(TipoPessoa.PESSOA_FISICA,'Maria',30,36000)
    pj = PessoaFactory.create(TipoPessoa.PESSOA_JURIDICA,'Nubank',9,100000)

    print(f'Valor a pagar de IR - Pessoa Física [{pf.nome}]: R${pf.calcularIR():.2f}')
    print(f'Valor a pagar de IR - Pessoa Jurídica [{pj.nome}]: R${pj.calcularIR():.2f}')


   