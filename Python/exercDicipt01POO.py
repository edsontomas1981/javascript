''# Exercício 06 da lista - Cronometro

# atributos: segundos, minutos, horas
# ações (métodos): construtor, representação,  incremento, start

'''import time
import os
class Cronometro:

    def __init__(self, segundos = 0, minutos = 0, horas = 0):
        self.segundos = segundos
        self.minutos = minutos
import time
import os
class Cronometro():
    def __init__(self,horas = 0,minutos = 0,segundos = 0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
    def tempo(self):
        if self.segundos < 59:
            self.segundos+=1
        else:
            self.segundos = 0
            self.minutos += 1
        if self.minutos > 59:
            self.minutos = 0
            self.horas += 1
            
    def __repr__(self):
        return f'{self.horas}:{self.minutos}:{self.segundos}'
    
    def start (self):
        while True :
            os.system('clear')
            print(self)
            self.tempo()
            time.sleep(1)
            

crono = Cronometro()
crono.start()
        self.horas = horas

    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
        

    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incremento()
            time.sleep(1)

cronometro1 = Cronometro()

cronometro1.start()
'''
class Agenda():
    def __init__(self):
        self.nome={}
        self.contatos = {}
        
    def incluir (self,nome,email,telefone):
        self.nome[nome]={nome:{'telefone':telefone,'email':email}}
    
    def alterar (self,nome):
        tel = input('Digite o novo numero de telefone : ')
        email=input('Digite o novo email : ')
        self.nome.update({nome:{'telefone':tel,'email':email}})
    
    def listaContatos(self):
        for printaContatos in self.nome:
            nome = printaContatos
            tel = self.nome[printaContatos]['telefone']
            email = self.nome[printaContatos].values()
            print(f'Nome : {nome} | Telefone : {tel} | Email {email}')
            
            
            
                
    def __repr__(self):
        return f'{self.nome}'
    
contato = Agenda()
contato.incluir('Edson','edson@edson','11-96926-2277')
contato.incluir('Sandra','sandra@edson','11-96926-2277')
contato.incluir('Ana','ana@edson','11-96926-2277')
contato.listaContatos()


