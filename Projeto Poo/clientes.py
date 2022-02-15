import json
import os.path
import sys
from datetime import datetime
def dataHoraLoc ():
    data = datetime.now()
    dataFormatada = data.strftime('%d/%m/%Y %H:%M')
    return dataFormatada
   
def carregaDados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados
dados = carregaDados()
def estoque():
    qtdeEstoque = 0
    for i in range (len(dados)):
        if dados[i]['status'] == 0:
            qtdeEstoque += 1
    return qtdeEstoque

class Cliente:
    pedido = 0       
    def __init__(self,nome,tipoAluguel):
        self.nome = nome
        self.tipoAluguel = tipoAluguel # 1 por hora |2 por Dia | 3 por semana |4 Familia 
        self.bicicletas = []
        self.diaLocacao = ''
        self.horaLocacao = ''
        
    
    def __repr__(self):
        tipoLocacao = 0
        nome = self.nome
        qtde = len(self.bicicletas)
        resposta = ''
        for i in range(len(self.bicicletas)):
            id = self.bicicletas[i]['id']
            marca = self.bicicletas[i]['marca'] 
            categoria = self.bicicletas[i]['categoria'] 
            cor = self.bicicletas[i]['cor'] 
            resposta += 'Id: '+id+'| Marca: '+marca+'| Categoria: '+categoria+'| Cor: '+cor+'\n'            
        if self.tipoAluguel == 1:
            tipoLocacao = 'por hora'
        elif self.tipoAluguel == 2:
            tipoLocacao = 'por dia'
        elif self.tipoAluguel == 3:
            tipoLocacao = 'por semana'
        return f'{nome} sua nodalidade de locação é {tipoLocacao} você tem o total de {qtde} bikes locadas \n {resposta} '

    def verBicicletas (self):
        bikesDisponiveis = ''
        for i in range (len(dados)):
            status =  dados[i]['status']
            if status == 0 :
                id = dados[i]['id']
                marca = dados[i]['marca']
                categoria = dados[i]['categoria']
                cor = dados[i]['cor']
                bikesDisponiveis += 'Id : '+id+'| Marca : ' +marca+'| Categoria : '+categoria+ '| Cor : '+cor +'\n'
        return bikesDisponiveis
    
    def gerarPedido (self,Bikes:list,dtLoc):
        pass           
    
    def alugarBicicletas (self,qtde):
        qtdeEmEstoque = estoque()
        dtLoc = dataHoraLoc()
        if qtde <= qtdeEmEstoque:
            for i in range (qtde):
                self.bicicletas.append({self.nome:{dados[i]}})
                dados[i]['status'] = 1
            print (self.bicicletas)
            return 'Locação efetuada com sucesso !'
        else:
            return 'Estoque indisponível'



cliente = Cliente('Edson Tomas',1)
cliente.alugarBicicletas(15)
cliente.verBicicletas()
print(cliente.verBicicletas())
print(cliente)


   
