import estoque

class Loja:
    def __init__(self):
        self.estoque = estoque.Estoque()
    @staticmethod
    def strValPag (tempoAluguel,tipoAluguel,qdteBikesDevolvidas,valorPagar):
        return f'O periodo de locação foi de {tempoAluguel} {tipoAluguel}.\n'\
        f'A quantidade de bicicletas alugadas foram de {qdteBikesDevolvidas} bicicletas\n'\
        f'O valor a ser pago é de R$ {valorPagar:.2f}'        
    def exibeEstoque(self):
        self.estoque.exibeEstoqueDisponivel()
    def alugaBikes(self,qtde,cliente):
        msg=self.estoque.alugaBikes(qtde,cliente)
        return msg
    def devolveBikes(self,cliente):
        qdteBikesDevolvidas = self.estoque.devolveBikes(cliente)
        tipoAluguel = cliente.tipoAluguel
        tempoAluguel= cliente.tempoAluguel
        
        if tipoAluguel == 1: # aluguel por hora 
            if qdteBikesDevolvidas < 3:
                valorPagar = (tempoAluguel*qdteBikesDevolvidas)*5
                return Loja.strValPag(tempoAluguel,'horas',qdteBikesDevolvidas,valorPagar)
            else:
                valorPagar = (tempoAluguel*qdteBikesDevolvidas)*5
                valorPagar = valorPagar-(valorPagar*30/100)
                return Loja.strValPag(tempoAluguel,'horas',qdteBikesDevolvidas,valorPagar)
        
        elif tipoAluguel == 2: # aluguel por dia 
            if qdteBikesDevolvidas < 3:
                valorPagar = (tempoAluguel*qdteBikesDevolvidas)*25
                return Loja.strValPag(tempoAluguel,'dias',qdteBikesDevolvidas,valorPagar)
            else:
                valorPagar = (tempoAluguel*qdteBikesDevolvidas)*25
                valorPagar = valorPagar-(valorPagar*30/100)
                return Loja.strValPag(tempoAluguel,'dias',qdteBikesDevolvidas,valorPagar)
        
        elif tipoAluguel == 3: # aluguel por semana
            if qdteBikesDevolvidas < 3:
                valorPagar = (tempoAluguel*qdteBikesDevolvidas)*5
                return Loja.strValPag(tempoAluguel,'semanas',qdteBikesDevolvidas,valorPagar)
            else:
                valorPagar = (tempoAluguel*qdteBikesDevolvidas)*5
                valorPagar = valorPagar-(valorPagar*30/100)
                return Loja.strValPag(tempoAluguel,'semanas',qdteBikesDevolvidas,valorPagar)
    def relatEstoque(self):
        self.estoque.relatorioEstoque()

class Cliente:
    def __init__(self,nome,tipoAluguel,tempoAluguel):
        self.nome = nome
        self.tipoAluguel = tipoAluguel # 1 por hora |2 por Dia | 3 por semana
        self.tempoAluguel = tempoAluguel
    def __repr__(self):
        if self.tipoAluguel == 1:
            aluguel = 'por hora'
            return f'[{self.nome},{aluguel},{self.tempoAluguel}]' 
        elif self.tipoAluguel == 2:
            aluguel = 'por dia'
            return f'[{self.nome},{aluguel},{self.tempoAluguel}]' 
        elif self.tipoAluguel == 3:
            aluguel = 'por semana'
            return f'[{self.nome} ,{aluguel},{self.tempoAluguel}]' 
    def verEstoque(self,loja):
        loja.exibeEstoque()
    def alugarBikes(self,loja,qtde):
        loja.alugaBikes(qtde,self)
    def relatCliente(self,loja):
        est = loja.estoque.estoque
        pedido = ''
        for i in est:
            if self.nome == i['alugadaPor']:
                print(i)
              
#Criação dos clientes 
#1º parametro nome
#2º parametro tipo de locação sendo que 1 para locação por hora,2 para locação por dia e 3 para locação semanal
#3º parametro trata do tempo de locação,valor inteiro que é diferenciado no momento do calculo pelo 2º parametro. 
cliente1 = Cliente('Edson Tomas',1,5)
cliente2 = Cliente('Ana Tomas',2,5)
loja1 = Loja()
# Chamadas a partir do objeto cliente
cliente1.verEstoque(loja1)
print('--------------------------------------------------------')
cliente1.alugarBikes(loja1,2)
cliente1.relatCliente(loja1)
print('--------------------------------------------------------')
# Chamadas a partir do objeto loja
loja1.alugaBikes(3,cliente2)
print(loja1.alugaBikes(21,cliente1))#qtde de bicicletas maior que o estoque.
print('--------------------------------------------------------')
print(loja1.devolveBikes(cliente2))
print('--------------------------------------------------------')









