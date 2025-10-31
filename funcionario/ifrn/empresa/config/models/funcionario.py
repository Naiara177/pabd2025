from dataclasses import dataclass, asdict
from  datetime import datetime, data
from typing import Optional

@dataclass 
class Funcionario:

    _cpf: str 
    _pnome: str
    _unome: str 
    _data_nasc: date
    _endereco: str = "Macau-Rn"
    _salario: float = 1518.01
    _sexo: str = 'f'
    _cpf_supervisor: Optional[str] = None
    _numero_departamento: Optional[int] = None 
    _created_at: Optional[detetime] = None
    _updated_at: Optional[datatime] = None 

    #Funcionario --> JSON (dict)
    def to_dict(self) -> dict:
        return asdict(self)
    
    #JSON (dict) --> Funcionario
    def from_dict(self, data) -> 'Funcionario':
        return Funcionario(
            data.get('cpf'),
            data.get('pnome'),
            data.get('unome'),
            data.get('data_nasc'),
            data.get('endereco', "Macau-Rn"),
            data.get('salario', 1518.01),
            data.get('sexo', 'f'),
            data.get('cpf_supervisor'),
            data.get('numero_departamento'),
            data.get('created_at'),
        )
   
        def __str__(self) -> str:
            return f"Funcionario(cpf={self._cpf}, pnome={self._pnome}, unome={self._unome}, data_nasc={self._data_nasc}, endereco={self._endereco}, salario={self._salario}, sexo={self._sexo}, cpf_supervisor={self._cpf_supervisor}, numero_departamento={self._numero_departamento}, created_at={self._created_at}, updated_at={self._updated_at})"
            