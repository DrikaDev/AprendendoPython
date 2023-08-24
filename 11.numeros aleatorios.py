#fazer o importe do random
import random

numero = random.randint(0, 10) #aqui ele escolhe aleatoriamente numeros entre 0 e 10
print(numero)
print('=========')

lista = [10, 22, 5, 45, 7]
escolha = random.choice(lista) #aqui ele escolhe aleatoriamente apenas os numeros da lista.
print(escolha)