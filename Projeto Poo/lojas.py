import json
import os.path
import sys
import clientes
def pegaDados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados
dados = pegaDados()
class Loja:
    numPed = 0
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
    def qtdeEstoque():
            qtdeEstoque = 0
            for i in range (len(dados)):
                        status =  dados[i]['status']
                        if status == 0 :
                            qtdeEstoque+=1                  
            return qtdeEstoque
    
    @staticmethod
    def selecionaBikes (qtde,cliente):
        qtdeEmEstoque = Loja.qtdeEstoque()
        if qtde <= qtdeEmEstoque:
            for i in range (qtde):
                status = dados[i]['status']
                if status == 0 :
                    
                    cliente.bicicletas.append(dados[i])
                    dados[i]['status'] = 1
                    dados[i]['alugadaPor'] = cliente.nome
                    print(dados[i])
            return cliente.bicicletas
        else:
            return 'Estoque indisponível'
    def geraPedidos(self,qtde,cliente):
        numPed = Loja.numPed +1
        selBikes = Loja.selecionaBikes(qtde,cliente)
        pedido = [numPed,selBikes]
        loja.listaPedidos.append(pedido)
        #print(loja.listaPedidos)
        

loja = Loja()
#loja.relatorioBikes()
#loja.mostrarEstoque()
#print(clientes.cliente)
cliente3 = clientes.Cliente("Sandra Mara",1)
cliente4 = clientes.Cliente("Ana Tomas",1)

loja.geraPedidos(5,cliente3)
print('teste')
loja.geraPedidos(8,cliente4)




    