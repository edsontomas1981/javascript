import json
import os.path
import sys
import estoque
def obtemDados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados
dados = obtemDados()

class Loja:
    numPed = 10000
    estoque = []
    listaPedidos = []
    def __init__(self):
        pass
    def calculaConta(self):
        pass
    def mostrarbikesAlugadas():
        pass
    def relatorioBikes (self):
        for i in range (len(dados)):
                id = dados[i]['id']
                marca = dados[i]['marca']
                categoria = dados[i]['categoria']
                cor = dados[i]['cor']
                if dados[i]['status']!=0:
                   status = 'Alugada'
                else:
                    status = 'Livre'
                alugPor = dados[i]['alugadaPor']
                print(f'Id :{id}| Marca :{marca:9s} | Categoria : {categoria} | Cor : {cor:9s} | Status {status:9s} | Alugada Por : {alugPor}  ')
    def estoque():
        qtdeEstoque = 0
        for i in range (len(dados)):
            if dados[i]['status'] == 0:
                qtdeEstoque += 1
        return qtdeEstoque 
        















