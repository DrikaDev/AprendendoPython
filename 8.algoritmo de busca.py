#busca binária

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        #encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        #verifica se o valor procurado está a esquerda ou a direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True #se o valor for encontrado, ele para aqui
        
        return False #se o valor não for encontrado, então ele para aqui.