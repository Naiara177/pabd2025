from funcionario.funcionario import Funcionario

class Gerente(Funcionario):

  __slots__ = ['_senha', '_qtd_gerenciaveis']

  def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
    super().__init__(nome, cpf, salario)
    self._senha = senha
    self._qtd_gerenciaveis = qtd_gerenciaveis

  def get_bonificacao(self):
    return self._salario * 0.2

  def __str__(self):
      return f'{super().__str__()}\nGerente(Senha: {self._senha}, Qtd. Ger.: {self._qtd_gerenciaveis})'

  @property
  def senha(self):
      return self._senha

  @senha.setter
  def senha(self, senha):
      self._senha = senha

  @property
  def qtd_gerenciaveis(self):
      return self._qtd_gerenciaveis

  @qtd_gerenciaveis.setter
  def qtd_gerenciaveis(self, qtd_gerenciaveis):
      self._qtd_gerenciaveis = qtd_gerenciaveis