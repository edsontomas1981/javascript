import json
import os.path
import sys
def pegaDados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados
dados = pegaDados()
class Loja:
    numPed = 0
    pedidos = []
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
    def mostrarEstoque(self):
        qtdeEstoque = 0
        for i in range (len(dados)):
                    status =  dados[i]['status']
                    if status == 0 :
                        id = dados[i]['id']
                        marca = dados[i]['marca']
                        categoria = dados[i]['categoria']
                        cor = dados[i]['cor']
                        qtdeEstoque += 1
                        print(f'Id :{id}| Marca :{marca:9s} | Categoria : {categoria} | Cor : {cor}')
    def qtdeEstoque(self):
            qtdeEstoque = 0
            for i in range (len(dados)):
                        status =  dados[i]['status']
                        if status == 0 :
                            qtdeEstoque+=1                  
            return qtdeEstoque
    
    @staticmethod
    def listaBikesSelecionadas (self,qtde):
        qtdeEmEstoque = Loja.qtdeEstoque()
        if qtde <= qtdeEmEstoque:
            for i in range (qtde):
                self.bicicletas.append(dados[i])
                dados[i]['status'] = 1
            return self.bicicletas
        else:
            return 'Estoque indisponível'
    @staticmethod
    def pedidos(qtde):
        numPed = Loja.numPed +1
        selBikes = Loja.listaBikesSelecionadas(qtde)
        pedido = [numPed,selBikes]
        Loja.pedidos.append(pedido)
        print(Loja.pedidos)

loja = Loja()
#loja.relatorioBikes()
#loja.mostrarEstoque()
loja.pedidos(5)

    