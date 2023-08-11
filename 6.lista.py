#list comprehension - pode ser chamada de listcomp - cria uma nova lista com alterações a partir da primeira lista

linguagens = ['Python', 'Java', 'JavaScript', 'C#', 'Ruby']
print ('Antes da listcomp = ', linguagens)

linguagens = [item.lower() for item in linguagens]
print ('Depois da listcomp = ', linguagens)

#map
print('====Exemplo de map====')
linguagens = "Python Java JavaScript C C# Go Kothin Ruby".split()
nova_lista = map(lambda x: x.lower(), linguagens)
print(f'A nova lista é = {nova_lista}\n')
nova_lista = list(nova_lista)
print(f'Agora sim, a nova lista é essa: {nova_lista}')

#range() - cria um objeto numérico iterável. Usamos o list() para transformá-lo em uma lista com números
print('===range()====')
numeros = list(range(0, 21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)