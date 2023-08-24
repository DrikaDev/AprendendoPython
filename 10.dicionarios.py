#Em Python, dicionários são arrays associativos, ou seja, um determinado valor passa a ser vinculado a uma chave. 

dicionario_sites = {"Diego": "diegomariano.com"}

#No dicionário acima, a chave "Diego" foi vinculada ao valor "diegomariano.com". Assim, para imprimir o valor chame:
print('1', dicionario_sites['Diego']) # Sera impresso "diegomariano.com
print("============")

#Se o dicionário tiver vários elementos, você pode usar laços para imprimi-los:
dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}

print(dicionario_sites["Udemy"])
print("============")
print('2', dicionario_sites)
print("============")
 
for chave in dicionario_sites:
    print(chave)
print("============")

for i in dicionario_sites.values():
    print(i)
print("============")

for i in dicionario_sites.keys():
    print(i)
print("============")