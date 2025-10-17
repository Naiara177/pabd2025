from abc import ABC, abstractmethod

class Pessoa(ABC):
    __slots__ = ['_nome', '_cpf']

    def __init__(self, nome: str, cpf: str):
        self._name = nome   
        self._cpf = cpf

@abstractmethod
def _str__(self):
    return f'Pessoa(Nome: {self.nome}, CPF: {self.cpf})'

    @property               
    def name(self):
        return self._nome