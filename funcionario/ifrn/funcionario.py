from funcionario.ifrn.pessoa import Pessoa

class Funcionario(Pessoa):
    def _init_(self, cpf, siape): 
        super()._init_(name, cpf)
        self._siape = siape

