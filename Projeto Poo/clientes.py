import json
import os.path
import sys
from datetime import datetime
#import lojas
import estoque

class Cliente:
    def __init__(self,nome,tipoAluguel):
        self.nome = nome
        self.tipoAluguel = tipoAluguel # 1 por hora |2 por Dia | 3 por semana
        self.bicicletas = []
        self.diaLocacao = ''
        self.horaLocacao = ''
    def dataHoraLoc ():
        data = datetime.now()
        dataFormatada = data.strftime('%d/%m/%Y %H:%M')
        return dataFormatada    
    def gerarPedido (self,dtLoc):
        pass
    '''def __repr__(self):
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
        return f'{nome} sua modalidade de locação é {tipoLocacao} você tem o total de {qtde} bikes locadas \n {resposta} '''

edson = Cliente('Edson',1)
estoque.estoque1.selecionaBikes(5,edson)
estoque.estoque1.exibeEstoqueDisponivel()
estoque.estoque1.relatorioEstoque()

