import json
import os.path
import sys
def pegaDados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados
dados = pegaDados()

class Cliente:
    
    def __init__(self,nome):
        self.nome = nome
        self.tipoAluguel = 0 # 1 por hora |2 por Dia | 3 por semana.

    def verBicicletas (self,dados):
        for i in range (len(dados)):
            status =  dados[i]['status']
            if status == 0 :
                id = dados[i]['id']
                marca = dados[i]['marca']
                categoria = dados[i]['categoria']
                cor = dados[i]['cor']
                print(f'ID:{id}| Bicicleta:{marca} |Categoria:{categoria} |Cor:{cor}')

    def alugarBicicletas (self,tipoAluguel,dados,id):
        for i in range(len(dados)):
            if id in dados[i]['id']:
                dados[i].update({"status":1})
                print(dados[i])

            

cliente = Cliente('Edson Tomas')
cliente.alugarBicicletas(1,dados,'DE40+003')
   
