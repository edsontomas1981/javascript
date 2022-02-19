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
        