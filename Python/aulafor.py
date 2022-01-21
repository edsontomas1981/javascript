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
for cont in range (10):
    lista.append(geraNumRandomico())

lista_4_primeiros=lista[:4]
cinco_ultimos=lista[5:]
lista_par=[]
lista_impar=[]

for cont in range(10):
    par = lista[cont]%2
    if par == 0:
        lista_par.append(lista[cont])
    else:
        lista_impar.append(lista[cont])




lista.sort(reverse=True)
lista_reversa = lista

print (f"Os 4 primeiros numeros da lista são : {lista_4_primeiros}")
print (f"Os 5 ultimos numeros da lista são : {cinco_ultimos}")
print (f"Os 5 ultimos numeros da lista são : {cinco_ultimos}")
print (f"Os numeros pares da lista são : {lista_par}")
print (f"Os numeros impares da lista são : {lista_impar}")
print (f"A lista em ordem reversa : {lista_reversa}")
print (f"A uma lista inversa dos 5 primeiros números : {lista_reversa[0:5]}")
print (f"A uma lista inversa dos 5 últimos números. : {lista_reversa[5:]}")





'''
f. uma lista inversa dos 5 primeiros números;

g. uma lista inversa dos 5 últimos números.
'''   