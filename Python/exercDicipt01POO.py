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
'''class Agenda():
    def __init__(self):
        self.nome={}
        self.contatos = {}
        
    def incluir (self,nome,email,telefone):
        self.nome[nome]={'telefone':telefone,'email':email}
    
    def alterar (self,nome):
        tel = input('Digite o novo numero de telefone : ')
        email=input('Digite o novo email : ')
        self.nome.update({nome:{'telefone':tel,'email':email}})
    
    def listaContatos(self):
        for printaContatos in self.nome:
            nome = printaContatos 
            tel = self.nome[printaContatos]['telefone']
            email = self.nome[printaContatos]['email']
            print(f'Nome : {nome}, E-mail :{email}, Telefone :{tel}')
            
    def buscaContato(self,nome):
        tel = self.nome[nome]['telefone']
        email = self.nome[nome]['email']
        return nome,tel,email
    def apagaContato(self,nome):
        del self.nome[nome]
    
    def __repr__(self):
        return f'{self.nome}'
    
contato = Agenda()
contato.incluir('Edson','edson@edson','11-96926-2277')
contato.incluir('Sandra','sandra@edson','11-96926-2277')
contato.incluir('Ana','ana@edson','11-96926-2277')
contato.apagaContato('Ana')
contato.listaContatos()'''
'''class Cliente:
    def __init__ (self,nome,idade,email) :
        self.nome = {nome:{'idade':idade,'E-mail':email}}
        
    def __repr__ (self):
        for elemento in self.nome:
            idade = self.nome[elemento]['idade']
            email = self.nome[elemento]['E-mail']
        return f' Nome : {elemento}\n Idade : {idade}\n E-mail : {email}'
cliente = Cliente('Edson',42,'edson@edson.com.br')
print(cliente)'''
'''

Vale
10
Enunciado
Com base no exercício anterior, crie um sistema de cadastro e a classe Cliente. Seu programa deve perguntar se o usuário quer cadastrar um novo cliente, alterar um cadastro ou sair.

Dica: Você pode fazer esse exercício criando uma classe Sistema, que irá controlar o sistema de cadastros. Essa classe deve ter o atributo cadastro e os métodos para imprimir os cadastrados, cadastrar um novo cliente, alterar um cadastro ou sair.
'''

    
'''
class Sistema:
    def __init__(self):
        self.cliente = ''
    def incluir (self,nome,idade,email):
        
        self.cliente = Cliente(nome,idade,email)
        
    def alterar (self,nome,idade,email):
        
        self.cliente.nome.update({nome:{'idade':idade,'email':email}})
        
iniciaSist = Sistema()
def menu():
    print('Digite 1 para incluir um novo cadastro : ')
    print('Digite 2 para alterar um cadastro : ')
    print('Digite 0 para sair : ')
    opcao = int(input('Digite sua opção : '))
    return opcao

opcao = menu() 

while opcao < 3 :
    if opcao == 1:
        nome = input('Digite o nome do cliente : ')   
        idade = input('Digite a idade : ')   
        email = input('Digite o email do cliente : ') 
        iniciaSist.incluir(nome,idade,email)
        opcao = menu() 
        
    elif opcao == 2:  
        nome = input('Digite o nome do cliente : ')   
        idade = input('Digite a idade : ')   
        email = input('Digite o email do cliente : ') 
        iniciaSist.alterar(nome,idade,email)
        opcao = menu() 
    elif opcao == 0:
        print(iniciaSist.cliente)
        print('Obrigado !')
        break'''

'''
Enunciado
Crie uma classe ContaCorrente com os atributos cliente 
(que deve ser um objeto da classe Cliente) e saldo. 
Crie métodos para depósito, saque e transferência. 
Os métodos de saque e transferência devem verificar se é possível realizar a transação.
'''
class Cliente:
    def __init__ (self,nome,idade,email) :
        self.nome = {nome:{'idade':idade,'email':email}}
        
    def __repr__ (self):
        for elemento in self.nome:
            idade = self.nome[elemento]['idade']
            email = self.nome[elemento]['email']
        return f' Nome : {elemento}\n Idade : {idade}\n E-mail : {email}'
    
class ContaCorrente:
    
    def __init__(self,cliente,saldo):
        self.saldo = float(saldo)
        self.cliente = cliente
        
    def __repr__(self):
        nome = self.cliente.nome
        saldo = self.saldo
        return f'O saldo do cliente {nome} é R${saldo}'
    
    def depositar(self,saldo):
        self.saldo += saldo
        
    def temSaldo(self):
        return self.saldo
        
    
        
    
        
    

cliente1 = Cliente('Edson',41,'edson@edson') 
cliente2 = Cliente('Ana',14,'ana@edson') 
cliente3 = Cliente('Sandra',14,'ana@edson')
cliente4 = Cliente('Gabriel',14,'ana@edson')
conta = ContaCorrente(cliente1,1000.00)
conta2=ContaCorrente(cliente2,2000.00)
conta.depositar(1100.00)
conta2.depositar(600.00)
print(conta)
print(conta2)


        



        
        




