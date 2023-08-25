#funções, são definidas pela palavra reservada 'def'

def soma( x, y):
    print(x)
    print(y)
    print ('Soma de x + y:', x + y)

soma(5, 2)
print('=========')

#função eval() - evaluation
#recebe como entrada uma string digitada pelo usuário - equação linear

# a = 2
# b = 1

# equacao = input('Digite a fórmula da equação linear (a * x + b): ')
# print(f'\nA entrada do usuário {equacao} é do tipo {type(equacao)}')

# for x in range(5):
#     y = eval(equacao)
#     print(f'\nResultado da equação para x = {x} é {y}')

print('=========')

#def para fazer função em Python

def imprimir_mensagem(disciplina, curso):
    print(f'Minha primeira função em Python desenvolvida na disciplina {disciplina}, do curso {curso} da Anhanguera.')

imprimir_mensagem("Linguagem de Programação", "ADS")

print('=========')

#enumerate
lista = ['bola', 'abacate', 'cachorro', 'python']
for i, nome in enumerate(lista):
    print(i, nome)

#map
print('=========')
print('Exemplo de map')

def dobro(x):
    return x * 2

valor = [1, 2, 3, 4, 5]
valor_dobrado = map (dobro, valor)
valor_dobrado = list (valor_dobrado)
print (valor_dobrado)

#reduce
print('=========')
#para obter a soma dos valores de uma lista:
#fazer o import:
from functools import reduce
def soma (x, y):
    return x + y
lista = [1, 3, 5, 10, 20]
soma = reduce(soma, lista)
print(soma) #resultado é 39

#zip - serve pra concatenar listas
#compacta duas ou mais listas para que possam ser analisadas ao mesmo tempo em um laço for
print('=========')
lista1 = [1, 2, 3, 4, 5]
lista2 = ['limão', 'bola', 'gato', 'Python', 'ficar rica']
lista3 = ['R$2,00', 'R$5,00', 'achar na rua', '27,90', 'estudar muito']

for numero, nome, valor in zip (lista1, lista2, lista3):
    print (numero, nome, valor)