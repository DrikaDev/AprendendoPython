#numpy

import numpy

matriz_1_1 = numpy.array([1, 2, 3]) #Cria 1 linha e 1 coluna
matriz_2_2 = numpy.array([1, 2], [3, 4]) #Cria 2 linhas e 2 colunas
matriz_3_2 = numpy.array([1, 2], [3, 4], [5, 6]) #Cria 3 linhas e 2 colunas
matriz_2_3 = numpy.array([1, 2, 3], [4, 5, 6]) #Cria 2 linhas e 3 colunas

print(type(matriz_1_1))
print('\n matriz_1_1 = ', matriz_1_1)
print('\n matriz_2_2 = \n', matriz_2_2)
print('\n matriz_3_2 = \n', matriz_3_2)
print('\n matriz_2_3 = \n', matriz_2_3)