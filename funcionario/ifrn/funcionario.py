from ifrn.pessoa import Pessoa

class Funcionario(Pessoa):
  def __init__(self, nome, cpf, siape):
    super().__init__(nome, cpf)
    self._siape = siape

  def __str__(self):
    return f'Funcionario({super().__str__()}, siape: {self._siape})'