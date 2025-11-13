from ifrn.pessoa import Pessoa

class Aluno(Pessoa):
  
  def __init__(self, nome, cpf, matricula):
    super().__init__(nome, cpf)
    self._matricula = matricula
  
  def __str__(self):
    return f'Aluno({super().__str__()}, matricula: {self._matricula})'