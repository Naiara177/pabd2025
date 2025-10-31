from empresa.config.database import SupabaseConnection
from empresa.dao.funcionario_dao import FuncionarioDAO

client = SupabaseConnection().client

# Criando DAO para acessar a tabela funcionario
funcionario_dao = FuncionarioDAO(client)

for funcionario in funcionario_dao.read_all():
  print(funcionario)

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