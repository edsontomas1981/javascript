import json
import os.path
import sys
from datetime import datetime


def carregaDados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados
dados = carregaDados()


class Cliente:
    pedido = []
    numPed = 0

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
        return f'{nome} sua modalidade de locação é {tipoLocacao} você tem o total de {qtde} bikes locadas \n {resposta} '

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
    
    def gerarPedido (self,dtLoc):
        bikes = {}
        pedido = [] 
        Cliente.numPed += 1
        for i in self.bicicletas:
            bikes = i
            Cliente.pedido.append({Cliente.numPed:{'Nome':self.nome,'bikes':self.bicicletas}})
        print(pedido)
    def listaBikesSelecionadas (self,qtde):
        qtdeEmEstoque = Cliente.estoque()
        dtLoc = Cliente.dataHoraLoc()
        if qtde <= qtdeEmEstoque:
            for i in range (qtde):
                self.bicicletas.append(dados[i])
                dados[i]['status'] = 1
            return self.bicicletas
        else:
            return 'Estoque indisponível'
    def dataHoraLoc ():
        data = datetime.now()
        dataFormatada = data.strftime('%d/%m/%Y %H:%M')
        return dataFormatada
    def estoque():
        qtdeEstoque = 0
        for i in range (len(dados)):
            if dados[i]['status'] == 0:
                qtdeEstoque += 1
        return qtdeEstoque
cliente = Cliente('Edson Tomas',2)

ped = cliente.listaBikesSelecionadas(5)
dat = Cliente.dataHoraLoc()
cliente.gerarPedido(dat)
cliente.gerarPedido(dat)




   
