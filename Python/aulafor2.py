'''
'''
def geraLista() :
    import random
    num = random.randrange(1, 101)
    lista=[]
    for i in range(num):
        lista.append(geraNumRandomico())
    return lista

def geraNumRandomico() :
    import random
    num = random.randrange(1, 1001)
    return num


lista=[]
maior50 = 0
media = 0
soma = 0
for cont in range (10):

    lista.append(geraNumRandomico())
    media += lista[cont]
    soma += lista[cont]
media/= 10   
print(lista)
print(f"O maior número sorteado é {max(lista)}")
print(f"O maior número sorteado é {min(lista)}")
print(f"O média dos números sorteados {media}")
print(f"O soma dos números sorteados {soma}")




'''
Faça um programa que sorteie 10 números entre 0 e 100 e imprima:

a. o maior número sorteado;

b. o menor número sorteado;

c. a média dos números sorteados;

d. a soma dos números sorteados.

Obs.: Precisa usar a biblioteca random
'''   