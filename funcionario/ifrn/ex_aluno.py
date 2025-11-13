from ifrn.pessoa import Pessoa

class ExAluno(Pessoa):
  
  def __init__(self, nome, cpf, curso):
    super().__init__(nome, cpf)
    self._curso = curso

  def __str__(self):
    return f'ExAluno({super().__str__()}, curso: {self._curso})'