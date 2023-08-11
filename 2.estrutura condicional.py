#condicional composta:
valor1 = 10
valor2 = 20

if valor1 > valor2:
    print ('O valor1 é maior que o valor2.')

else:
    print ('O valor2 é maior que o valor1.')

#estrutura encadeada, usamos o 'elif' que é uma abreviação do 'else if'
cor = 'qualquer cor'

if cor == 'verde':
    print ('Acelere')
elif cor == 'amarelo':
    print ('Atenção')
else:
    print ('Pare!')

#estrutura condicional usando operador booleano
#o aluno é aprovado se tiver menos que 5 faltas e média igual ou superior a 7
qtde_falta = int(input('Digite a quantidade de faltas: '))
media_final = float(input('Digite a média final: '))

if qtde_falta <= 5 and media_final >= 7:
    print ('Aluno aprovado!')
else:
    print ('Aluno reprovado!')