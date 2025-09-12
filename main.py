
# Revisão de Orientação a Objetos
# Naiara

frutas = ['Maçã', 'Banana', 'Laranja']
print(frutas)
print(frutas[0]) #pra pedir a ordem  e [ numero]
print(f'Tamanho: {len(frutas)}') #pedir tamanho e com a função len

frutas.append('Uva') #incerir um elemento
print(frutas)

frutas.insert(1, 'Abacaxi') #para inserir a ordem e o elemento
print(frutas)

# - remove o ultimo elemento da lista
#frutas.pop() # remove o último elemento da lista
#frutas.pop(0)  # remove o elemento do indice 0
frutas.remove('Laranja')
#print(f'Removido: {frutas}')
print(frutas)


numeros = [3,1,4,1,5,9,2,6,5,3]
print(numeros)

# Ordenar - crescente
numeros_ord_c = sorted(numeros)
print(f'Lista Ordenada (c): {numeros_ord_c}')

#Ordenar - decrecente
numeros_ord_d = sorted(numeros, reverse=True)
print(f'Lista Ordenada (d): {numeros_ord_d}')

#numeros_dobrados = []
#for n in numeros:
 #       numeros_dobrados.append(n*2)
#print(numeros_dobrados)
numeros_dobrados = list(map(lambda n: n*2, numeros)) 
print(numeros_dobrados)

#numeros_filtrados = [ ]
#for n in numeros:
 #   if n > 4:
  #      numeros_filtrados.append(n)
#print(numeros_filtrados)

numeros_filtrados = list(filter(lambda n: n > 4, numeros))
print(numeros_filtrados)

soma = 0 
for n in numeros:
    soma += n
print(f'Soma: {soma}')

print(soma)

from functools import reduce

soma = reduce(lambda soma, n: soma + n, numeros) # é o valor inicial  do acumulador
print(soma)  