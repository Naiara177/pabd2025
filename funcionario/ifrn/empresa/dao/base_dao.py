'''
  *** BaseDAO ***
  Classe abstrata base para DAOs (Data Access Objects)
  Operações CRUD genéricas
'''

from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from supabase import Client

# TypeVar - tornar a classe genérica
T = TypeVar('T')

class BaseDAO(ABC, Generic[T]):

  def __init__(self, client: Client, table_name: str):
    self._client = client
    self._table_name = table_name


  # Do formato JSON (dict) para modelo de dados (T)
  @abstractmethod
  def to_model(self, data: dict) -> T:
    pass

  # Do modelo de dados (T) para formato JSON (dict)
  @abstractmethod
  def to_dict(self, model: T) -> dict:
    pass
  ### Create
  # Insere um registro a partir do modelo e retorna o modelo criado
  def create(self, model: T) -> Optional[T]:
    try:
      payload = self.to_dict(model)
      response = self._client.table(self._table_name).insert(payload).execute()
      if response.data:
        # response.data pode ser lista ou dict dependendo do client
        data = response.data[0] if isinstance(response.data, list) else response.data
        return self.to_model(data)
      return None
    except Exception as e:
      print(f'Erro ao criar registro em {self._table_name}: {e}')
      return None

  ### Read
  # Retorna todos os valores de uma tabela
  def read_all(self) -> List[T]:
    try:
      response = self._client.table(self._table_name).select('*').execute()
      if response.data:
        return [self.to_model(item) for item in response.data]
      return []
    except Exception as e:
      print(f'Erro ao buscar todos os registros: {e}')
      return []
    
  ### Update
  # Atualiza um registro identificado por `id_field` (padrão 'id') e retorna o modelo atualizado
  def update(self, id_value, model: T, id_field: str = 'id') -> Optional[T]:
    try:
      payload = self.to_dict(model)
      response = self._client.table(self._table_name).update(payload).eq(id_field, id_value).execute()
      if response.data:
        data = response.data[0] if isinstance(response.data, list) else response.data
        return self.to_model(data)
      return None
    except Exception as e:
      print(f'Erro ao atualizar registro {id_value} em {self._table_name}: {e}')
      return None
  
  ### Delete
  # Remove um registro identificado por `id_field` (padrão 'id'). Retorna True se removido com sucesso.
  def delete(self, id_value, id_field: str = 'id') -> bool:
    try:
      response = self._client.table(self._table_name).delete().eq(id_field, id_value).execute()
      # Considera sucesso se não houver exceção e response.data for truthy (lista ou dict)
      if hasattr(response, 'data') and response.data:
        return True
      # Alguns clientes retornam lista vazia; considerar como sucesso se status_code for 204 ou 200
      if hasattr(response, 'status_code') and response.status_code in (200, 204):
        return True
      return False
    except Exception as e:
      print(f'Erro ao deletar registro {id_value} em {self._table_name}: {e}')
      return False