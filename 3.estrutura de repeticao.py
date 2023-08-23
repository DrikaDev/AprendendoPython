#laços de repetição
#Iteradores: iterar é repetir
#repetem um trecho do código enquanto uma condição avalidada for verdadeira

x = 1
while x <= 10:
    print (x)
    x = x + 1

print('==================')

numero = 1

while numero != 0:
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        print('Número par.')
    else:
        print('Número ímpar.')

print('==================')

#for seguido da variavel de controle'c'
nome = 'Adriana'

for c in nome:
    print(c)

print('==================')

#enumerate para retornar à posição de cada item dentro da sequência
nome = 'Nicolas'

for i, c in enumerate (nome):
    print(f'Posição = {i}, valor = {c}')

print('==================')

#break
disciplina = 'Linguagem de programação'

for c in disciplina:
    if c == 'a':
        break
    else:
        print(c)

print('==================')

#continue
linguagem = "Python"

for c in linguagem:
    if c == 'y':
        continue
    else:
        print(c)

print('==================')