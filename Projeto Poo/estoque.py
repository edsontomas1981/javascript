import json
import os.path
import sys

from grpc import ClientCallDetails
def obtemDados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

class Estoque:
    def __init__(self):
        self.estoque =  obtemDados()
    def relatorioEstoque (self):
        for i in range (len(self.estoque)):
                id = self.estoque[i]['id']
                marca = self.estoque[i]['marca']
                categoria = self.estoque[i]['categoria']
                cor = self.estoque[i]['cor']
                if self.estoque[i]['status']!=0:
                   status = 'Alugada'
                else:
                    status = 'Livre'
                alugPor = self.estoque[i]['alugadaPor']
                print(f'Id :{id}| Marca :{marca:9s} | Categoria : {categoria} | Cor : {cor:9s} | Status {status:9s} | Alugada Por : {alugPor}  ')
    def exibeEstoqueDisponivel(self):
        for i in range (len(self.estoque)):
            status =  self.estoque[i]['status']
            if status == 0 :
                id = self.estoque[i]['id']
                marca = self.estoque[i]['marca']
                categoria = self.estoque[i]['categoria']
                cor = self.estoque[i]['cor']
                print(f'Id :{id}| Marca :{marca:9s} | Categoria : {categoria} | Cor : {cor}')
    
    def selecionaBikes (self,qtde,cliente):
        disponivelEstoque = self.qtdeEmEstoque()
        if qtde <= disponivelEstoque:
            cont = 0
            i=0
            while cont < qtde :
                status =self.estoque[i]['status']
                if status == 0 :
                    self.estoque[i]['status'] = 1
                    self.estoque[i]['alugadaPor'] = cliente.nome
                    cont += 1
                i += 1 
        else:
            return 'Estoque indisponível'
    def qtdeEmEstoque(self):
        qtdeEstoque = 0
        for i in range (len(self.estoque)):
            if self.estoque[i]['status'] == 0:
                qtdeEstoque += 1
        return qtdeEstoque 
estoque1=Estoque()
#estoque1.relatorioEstoque()
        
