class Funcionario:
  
  __slots__ = ['_nome', '_cpf', '_salario']

  def __init__(self, nome, cpf, salario):
    self._nome = nome
    self._cpf = cpf
    self._salario = salario
  
  def get_bonificacao(self):
    return self._salario * 0.1

  def __str__(self):
    return f'Funcionario(Nome: {self._nome}, CPF: {self._cpf}, Salário: {self._salario:.2f})'

  @property
  def nome(self):
    return self._nome
  
  @nome.setter
  def nome(self, nome):
    self._nome = nome

  @property
  def cpf(self):
    return self._cpf
  
  @cpf.setter
  def cpf(self, cpf):
    self._cpf = cpf

  @property
  def salario(self):
    return self._salario
  
  @salario.setter
  def salario(self, salario):
    self._salario = salario