"""Exemplos de CRUD para `funcionario` e `departamento`.

Este script tenta conectar ao Supabase usando `SupabaseConnection`.
Se as variáveis de ambiente não estiverem configuradas, usa um cliente mock em memória
para demonstração dos métodos CRUD via `BaseDAO`/DAOs específicos.
"""

from datetime import datetime
from typing import Any, Dict
import os
import sys

# Ajusta sys.path para encontrar o package `empresa` dentro de `funcionario/ifrn`
ROOT = os.path.dirname(__file__)
PACKAGE_ROOT = os.path.join(ROOT, 'funcionario', 'ifrn')
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)

try:
    from empresa.config.database import SupabaseConnection
    from empresa.dao.funcionario_dao import FuncionarioDAO
    from empresa.dao.departamento_dao import DepartamentoDAO
    REAL_CLIENT = True
except Exception:
    # Se ocorrer erro ao importar (ex.: variáveis de ambiente ausentes), usaremos mock
    REAL_CLIENT = False


class _MockResponse:
    def __init__(self, data=None, status_code=200):
        self.data = data
        self.status_code = status_code


class _MockTable:
    def __init__(self, client: 'MockClient', name: str):
        self.client = client
        self.name = name
        self._operation = None
        self._payload = None
        self._eq_field = None
        self._eq_value = None

    def select(self, *args, **kwargs):
        self._operation = 'select'
        return self

    def insert(self, payload: Dict[str, Any]):
        self._operation = 'insert'
        self._payload = payload
        return self

    def update(self, payload: Dict[str, Any]):
        self._operation = 'update'
        self._payload = payload
        return self

    def delete(self):
        self._operation = 'delete'
        return self

    def eq(self, field: str, value: Any):
        self._eq_field = field
        self._eq_value = value
        return self

    def execute(self):
        store = self.client._store.setdefault(self.name, [])
        if self._operation == 'select':
            # retorna todos os registros
            return _MockResponse(list(store))

        if self._operation == 'insert':
            item = dict(self._payload)
            # atribui id incremental quando aplicável (numero) ou mantém cpf
            if 'numero' in item and not item.get('numero'):
                # next number
                next_num = (max((r.get('numero') or 0) for r in store) + 1) if store else 1
                item['numero'] = next_num
            store.append(item)
            return _MockResponse([item], 201)

        if self._operation == 'update':
            updated = []
            for idx, r in enumerate(store):
                if self._eq_field and r.get(self._eq_field) == self._eq_value:
                    new = dict(r)
                    new.update(self._payload)
                    store[idx] = new
                    updated.append(new)
            return _MockResponse(updated)

        if self._operation == 'delete':
            removed = []
            new_store = []
            for r in store:
                if self._eq_field and r.get(self._eq_field) == self._eq_value:
                    removed.append(r)
                else:
                    new_store.append(r)
            self.client._store[self.name] = new_store
            return _MockResponse(removed)


class MockClient:
    def __init__(self):
        self._store = {}

    def table(self, name: str) -> _MockTable:
        return _MockTable(self, name)


def _print_section(title: str):
    print('\n' + '=' * 10 + ' ' + title + ' ' + '=' * 10)


def main():
    # obter client real ou mock
    if REAL_CLIENT:
        client = SupabaseConnection().client
        # testar se a conexão é realmente utilizável; se houver erro (ex: chave inválida), usar mock
        try:
            probe = client.table('departamento').select('*').execute()
            # se responder com status_code 401/403 ou payload de erro, considere inválido
            bad_status = getattr(probe, 'status_code', None) in (401, 403)
            bad_data = isinstance(getattr(probe, 'data', None), dict) and probe.data.get('code') in (401, 403)
            if bad_status or bad_data:
                raise Exception('Supabase probe retornou erro')
            print('Usando Supabase real (variáveis de ambiente detectadas)')
        except Exception:
            print('Aviso: não foi possível usar Supabase real — usando mock para demonstração')
            client = MockClient()
    else:
        client = MockClient()
        print('Usando cliente mock (modo demonstração)')

    # importar DAOs (evita erro caso import anterior falhe)
    from empresa.dao.departamento_dao import DepartamentoDAO
    from empresa.dao.funcionario_dao import FuncionarioDAO

    dep_dao = DepartamentoDAO(client)
    func_dao = FuncionarioDAO(client)

    # --- Create ---
    _print_section('CREATE')
    from empresa.models.departamento import Departamento
    from empresa.models.funcionario import Funcionario

    novo_dep = Departamento(numero=None, nome='Engenharia', localizacao='Bloco A')
    criado_dep = dep_dao.create(novo_dep)
    print('Departamento criado:', criado_dep)

    novo_func = Funcionario(cpf='12345678900', pnome='Ana', unome='Silva', numero_departamento=criado_dep.numero if criado_dep else None)
    criado_func = func_dao.create(novo_func)
    print('Funcionario criado:', criado_func)

    # --- Read ---
    _print_section('READ ALL')
    deps = dep_dao.read_all()
    funcs = func_dao.read_all()
    print('Departamentos:', deps)
    print('Funcionarios:', funcs)

    # --- Update ---
    _print_section('UPDATE')
    if deps:
        first = deps[0]
        # alterar nome
        first.nome = first.nome + ' (Atualizado)'
        updated = dep_dao.update(first.numero, first, id_field='numero')
        print('Departamento atualizado:', updated)

    if funcs:
        f = funcs[0]
        f.pnome = f.pnome + ' Maria'
        updated_f = func_dao.update(f.cpf, f, id_field='cpf')
        print('Funcionario atualizado:', updated_f)

    # --- Delete ---
    _print_section('DELETE')
    if funcs:
        cpf = funcs[0].cpf
        ok = func_dao.delete(cpf, id_field='cpf')
        print(f'Delete funcionario {cpf}:', ok)

    if deps:
        num = deps[0].numero
        ok2 = dep_dao.delete(num, id_field='numero')
        print(f'Delete departamento {num}:', ok2)


if __name__ == '__main__':
    main()

"""
from conta import Conta
from cliente import Cliente
from empresa.config.database import SupabaseConnection
from funcionario.controle_de_bonificacoes import ControleDeBonificacoes
# from funcionario.funcionario import Funcionario
from funcionario.gerente import Gerente
from ifrn.pessoa import Pessoa
from ifrn.funcionario import Funcionario

# Aula 17/10 - Polimorfismo, Classes Abstratas, Supabase

client = SupabaseConnection().client

# pessoa = Pessoa('Guilherme', '111.222.333-44')
# print(pessoa)

# f = Funcionario('Guilherme', '111.222.333-44', '1886519')
# print(f)

# f = Funcionario('Bartô Galeno', '111.222.333-44', 50000)
# print(f.get_bonificacao())
# print(f)
# g = Gerente('Reginaldo Rossi', '777.222.333-88', 250000, 1234, 10)
# print(g.get_bonificacao())
# print(g)

# controle = ControleDeBonificacoes()
# controle.registra(f)
# controle.registra(g)
# print(f'Total = R$ {controle.total:.2f}')

# cliente1 = Cliente("Elvis Presley", "111.222.333-44")
# controle.registra(cliente1)



# Aula 10/10 - Métodos estáticos, métodos de classe
# Herança e Reescrita de métodos

f = Funcionario('Bartô Galeno', '111.222.333-44', 50000)
print(f.get_bonificacao())
print(f)
g = Gerente('Reginaldo Rossi', '777.222.333-88', 250000, 1234, 10)
print(g.get_bonificacao())
print(g)

#  cliente1 = Cliente("Elvis Presley", "111.222.333-44")
# conta1 = Conta(cliente1, 1, 123, "elvis@gmail.com", 10000)
# print(Conta.total_contas())
# cliente2 = Cliente("Jonhny Cage", "222.333.444-55")
# conta2 = Conta(cliente2, 2, 234, "jonhnny@outlook.com", 5000)
# print(Conta.total_contas())

# print(Conta.lista_contas()[0].saldo)
# print(Conta.lista_contas()[1].saldo)

# print(Conta.get_saldo_total())

# print(Conta.total_contas_cm())


# Aula 26/09 - Agregação, Composição, Modificadores de Acesso
cliente1 = Cliente("Elvis Presley", "111.222.333-44")
conta1 = Conta(cliente1, 1, 123, "elvis@gmail.com", 10000)
conta1.extrato()
conta1.saca(500)
conta1.deposita(300)

cliente2 = Cliente("Jonhny Cage", "222.333.444-55")
conta2 = Conta(cliente2, 2, 234, "jonhnny@outlook.com", 5000)
conta2.extrato()
conta2.saca(100)
conta2.deposita(600)

conta1.transfere(conta2, 2000)
conta2.saca(10000)

conta1.historico.imprime()
conta2.historico.imprime()

# sem decorator
conta1.set_saldo(-100)
print(conta1.get_saldo()) #getter
print(conta1.get_saldo()*1.1 + conta2.get_saldo()*0.9)

# com decorator
conta1.saldo = -100
print(conta1.saldo) #getter
print(conta1.saldo*1.1 + conta2.saldo*0.9)

# Aula 19/09 - Orientação a Objetos


cliente1 = Cliente('Elvis Presley', '111.222.333-44')
conta1 = Conta(cliente1, 1, 123, 'elvis@gmail.com', 12345678)
conta1.extrato()
# conta1.deposita(100)
# conta1.extrato()

# conta2 = conta1
# conta2.extrato()
# conta2.saca(100)
# conta2.extrato()
# conta1.extrato()

# if(conta1.saca(1000)):
#     print('OK')
# else:
#     print('Tá Liso')

cliente2 = Cliente('Jonhny Cage', '222.333.444-55')
conta2 = Conta(cliente2, 2, 234, 'jonhnny@outlook.com', 234567)
conta2.extrato()

if(conta2.transfere(conta1, 1000)):
    print('OK')
else:
    print('Tá liso')

"""

"""
# Aula 12/092023 - Listas e Funções Lambda
frutas = ['Maçã', 'Banana', 'Laranja']
print(frutas)
print(frutas[0])
print(f'Tamanho: {len(frutas)}')

frutas.append('Uva')
print(frutas)

frutas.insert(0, 'Abacaxi')
print(frutas)

# -> Remove último elemento da lista
# fruta = frutas.pop() 
# -> Remove elemento do índice 0
# fruta = frutas.pop(0)
frutas.remove('Laranja')
# print(f'Removido: {fruta}')
print(frutas)

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numeros)

# Ordenar - crescente
numeros_ord_c = sorted(numeros)
print(f'Lista ordenada (c): {numeros_ord_c}')

# Ordenar - decrescente
numeros_ord_d = sorted(numeros, reverse=True)
print(f'Lista ordenada (d): {numeros_ord_d}')

# numeros_dobrados = []
# for n in numeros:
#     numeros_dobrados.append(n*2)
numeros_dobrados = list(map(lambda n: n*2, numeros))
print(numeros_dobrados)

# numeros_filtrados = []
# for n in numeros:
#     if n > 4:
#         numeros_filtrados.append(n)
numeros_filtrados = list(filter(lambda n: n > 4, numeros))
print(numeros_filtrados)

soma = 0
for n in numeros:
    soma += n
print(soma)

from functools import reduce

soma = reduce(lambda soma, n: soma + n, numeros)
print(soma)
"""