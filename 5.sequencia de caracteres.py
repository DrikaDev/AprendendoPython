#objetos do tipo sequência de caracteres

texto = "Estou aprendendo Python na disciplina de linguagem de programação da faculdade Anhanguera"
print(f'Tamanho do texto = {len(texto)}')
print(f'Python in texto = {"Python" in texto}')
print(f'Quantidade de y no texto = {texto.count("y")}')
print(f'As 5 primeiras letras são: {texto[0:6]}')

#função split - usada para cortar um texto e transformá-lo em lista

palavras = texto.split()
print(f'palavras = {palavras}')
print(f'Quantidade de palavras = {len(palavras)}')

print('===================')

#função index - retorna a posição de um valor na sequência

vogais = ['a', 'e', 'i', 'o', 'u']
for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')




