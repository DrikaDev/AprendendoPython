#while: usado para construir e controlar uma estrutura de decisão sempre que 
#o numero de repetições for desconhecido

numero = 1

while numero != 0:
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        print('Número par.')
    else:
        print('Número ímpar.')

#for seguido da variavel de controle'c'
nome = 'Adriana'

for c in nome:
    print(c)

#enumerate para retornar à posição de cada item dentro da sequência
nome = 'Nicolas'

for i, c in enumerate (nome):
    print(f'Posição = {i}, valor = {c}')

#break
disciplina = 'Linguagem de programação'

for c in disciplina:
    if c == 'g':
        break
    else:
        print(c)

#continue
linguagem = "Python"

for c in linguagem:
    if c == 'y':
        continue
    else:
        print(c)
