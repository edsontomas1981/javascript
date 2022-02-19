import json
import os.path
import sys
import clientes

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
    def alugaBikes (self,qtde,cliente):
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
            return 'Operaçã efetuada com sucesso' 
        else:
            return 'Estoque indisponível'
    def qtdeEmEstoque(self):
        qtdeEstoque = 0
        for i in range (len(self.estoque)):
            if self.estoque[i]['status'] == 0:
                qtdeEstoque += 1
        return qtdeEstoque 
    def devolveBikes(self,cliente):
        qtdeBikesDevolvidas = 0
        nome = cliente.nome
        for i in range (len(self.estoque)):
            if nome == self.estoque[i]['alugadaPor']:
                self.estoque[i]['status'] = 0
                self.estoque[i]['alugadaPor'] = ''
                qtdeBikesDevolvidas += 1
        return qtdeBikesDevolvidas


        
