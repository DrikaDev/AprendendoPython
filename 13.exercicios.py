#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.
idade = int(input('Digite sua idade:'))
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

print('========')
#Faça um programa que receba duas notas digitadas pelo usuário. 
# Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1+nota2) / 2
if media >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')

print('========')
#Escreva um programa que resolva uma equação de segundo grau.
from math import sqrt
a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B:'))
c = int(input('Digite o valor de C:'))

delta = b**2 - 4*a*c
if delta < 0:
    print('Delta negativo.')
else:
    raiz_delta = sqrt(delta)
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b - raiz_delta)/2*a
    print('As raízes são:', x1, 'e', x2)

print('========')
#Escreva um programa que ordene uma lista numérica com três elementos.
lista = ['Nicolas', 'Adriana', 'Cassio']
print(sorted(lista))

print('========')
#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
n1 = int(input('Digite o primeiro número: '))
sinal = input('Digite o sinal matemático que deseja:')
n2 = int(input('Digite o segundo numero: '))

if sinal == '+':
    op = n1 + n2
elif sinal == '-':
    op = n1 - n2
elif sinal == '/':
    op = n1 / n2
elif sinal == '*':
    op = n1 * n2
else:
    print('Sinal inválido!')

print (op)