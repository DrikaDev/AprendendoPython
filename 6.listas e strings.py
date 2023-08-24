#listas representam um conjunto de dados

lista1 = [1, 2, 3, 4, 5]
lista2 = [0, 'olá', 'mundo', 9.99, True]

for i in lista1:
    print("lista1", lista1)

print('==================')

for i in lista2:
    print('lista2', lista2)

print('==================')

#list comprehension - pode ser chamada de listcomp - cria uma nova lista com alterações a partir da primeira lista

linguagens = ['Python', 'Java', 'JavaScript', 'C#', 'Ruby']
print ('Antes da listcomp = ', linguagens)

linguagens = [item.lower() for item in linguagens]
print ('Depois da listcomp = ', linguagens)

print('==================')

#map
print('====Exemplo de map====')
linguagens = "Python Java JavaScript C C# Go Kothin Ruby".split()
nova_lista = map(lambda x: x.lower(), linguagens)
print(f'A nova lista é = {nova_lista}\n')
nova_lista = list(nova_lista)
print(f'Agora sim, a nova lista é essa: {nova_lista}')

print('==================')

#range - na faixa de 10 a 20, pulando de 2 em 2, ex:
for i in range(10, 20, 2):
    print('O range de 10 a 20 é: ', i)

print('==================')

#range() - cria um objeto numérico iterável. 
# Usamos o list() para transformá-lo em uma lista com números
numeros = list(range(0, 21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print('O range dos números pares é: ', numeros_pares)

print('==================')

#Strings é um tipo de dado declarado entre aspas e que armazemos caracteres (texto)
#verificando o tamanho de uma string com len:
nome = 'Adriana'
sobrenome = 'Gutierrez'

concatenar = nome + '-' + sobrenome
tamanho = len(concatenar)
print ('A quantidade de letras de Adriana Gutierrez é: ', tamanho)
print ('Navegando pelo indíce: ', nome [4])
print ('Imprimindo parte da string: ', nome [0:4])

print (concatenar)
print ('Imprimindo em letras maiúsculas: ',concatenar.upper());

print('==================')

#.strip remove espaço indesejado
#ex: print(concatenar.strip())

#.split converte uma string em em uma lista
minha_string = 'O rato roeu a roupa do/a rei de Roma.'
minha_lista = minha_string.split()
print(minha_lista)

minha_lista = minha_string.split('r')
print(minha_lista)

print('==================')

#Buscando substrings - pedaço de uma string:
#Ex: em que posição/índice aparece a palavra 'rei'?
busca = minha_string.find('rei')
print ('A palavra rei está na posição: ', busca)

print ('Tudo que vem depois da palavra rei:', minha_string[busca:])

print('==================')

#Substituir partes de uma string:
#método .replace
print('Substituir rei pela palavra rainha:', minha_string.replace('rei', 'rainha'))
print('==================')

#len para verificar o tamanho da lista:
lista_frutas = ['banana', 'abacaxi', 'uva', 'melancia']
print(lista_frutas)
print(lista_frutas[3])
print('==================')
for item in lista_frutas:
    print(item)
print('==================')
tamanho = len(lista_frutas)
print(tamanho)
print('==================')

#reverse
lista_frutas.sort()
print("lista ordenada", lista_frutas)
lista_frutas.sort(reverse=True)
print("lista invertida", lista_frutas)
print('==================')

#.append - para adicionar elementos ao final da lista
lista_frutas.append('limão')
print(lista_frutas)
print('==================')

#verificando se um elemento pertence a uma lista
if 'limão' in lista_frutas:
    print('Esta fruta está na lista.')

#apagando um elemento da lista
del lista_frutas[3] #aqui deleta apenas o item 3
print (lista_frutas)
del lista_frutas[2:] #aqui deleta do item 2 em diante
print (lista_frutas)
del lista_frutas[:] #aqui deleta a lista inteira
print (lista_frutas)

print('==================')
#criando lista vazia
lista_vazia = []
lista_vazia.append("Adriana") #adicionando um item a lista_vazia
print(lista_vazia)
print('==================')

#sort para ordenar a lista numericamente
lista_valores = [4, 9, 501, 102, 322, 546, 5, 27, 17, 56, 2]
lista_valores.sort()
print(lista_valores)
#reverse para ordenar a lista de trás pra frente/para reverter
lista_valores.sort(reverse=True)
print(lista_valores)
#inverter a lista
lista_valores.reverse()
print(lista_valores)

