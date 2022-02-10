'''
1. Classe Bola: Crie uma classe que modele uma bola:
    - Atributos: Cor, circunferência, material
    - Métodos: trocaCor e mostraCor

'''
'''class Bola:
    def __init__(self,cor,circ,mat) :
        self.cor = cor
        self.circ = circ
        self.mat = mat
    def trocaCor(self,novaCor):
        self.cor = novaCor
    def mostraCor(self):
        print(f'A cor da bola é {self.cor}')
'''
'''
2. Classe Quadrado: Crie uma classe que modele um quadrado:
    - Atributos: Tamanho do lado
    - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''
'''class Quadrado:
    def __init__(self,lado):
        self.lado = lado
    def mudaValorLado(self,novoLado):
        self.lado = novoLado
    def tamanhoLado(self):
        return self.lado
    def calculaArea(self):
        return self.lado * self.lado

q1 = Quadrado(2)
print(q1.tamanhoLado())
print(q1.calculaArea())
q1.mudaValorLado(3)
print(q1.tamanhoLado())
print(q1.calculaArea())'''
'''
3. Classe Retangulo: Crie uma classe que modele um retangulo:
    - Atributos: Tamanho do lado
    - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
    - Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
    Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local. 
    O programa também deve pedir as medidas de cada piso e rodapé
'''

class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def area(self):
        area = base * altura
        return float(area)
    def areaLinear (self):
        return float((self.base*2)+(self.altura*2))

base = float(input('Informe o tamanho da base : '))
altura = float(input('Informe o tamanho da altura : '))
areaRetangulo = Retangulo(5,25)


def areaPiso():
    pisoBase = input('Informe a base do piso : ')
    pisoAltura = input('Informe a altura do piso : ')
    areaPiso = pisoAltura*pisoBase
    return areaPiso

piso = areaPiso()
rodape = float(input('Informe o tamanho do rodapé : '))

areaRet = areaRetangulo.area
areaLin = areaRetangulo.areaLinear
qtdePiso = float(areaRet)/piso
qtdeRodape = float(areaLin)/rodape

print(f' {qtdePiso} , {qtdeRodape} ')






'''
4. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente
    - Atributos: número da conta, nome do correntista e saldo
    - Métodos: alterar_nome, deposito e saque; No construtor, saldo é opcional, 
    com valor default zero e os demais atributos são obrigatórios.
'''
'''class contaCorrente:
    def __init__(self,conta,nome,saldo = 0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo
    def alterarNome(self,novoNome):
        self.nome = novoNome
    def deposito(self,valor):
        self.saldo += valor
    def saque(self,valor):
        if self.saldo>valor:
            self.saldo -= valor
        else:
            print('Saldo inferior ao valor do saque !')

correntista = contaCorrente('07225','Edson Tomas da Silva')
correntista.deposito(3000.00)
print(correntista.saldo)
correntista.saque(600.00)
print(correntista.saldo)'''

'''
6. Classe Conta de Investimento: Faça uma classe ContaInvestimento que seja semelhante a classe de conta corrente, 
    com a diferença de que se adicione um atributo taxa_juros.
    Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. 
    Forneça um método adicione_juros (sem parâmetro explícito) que adicione juros à conta. 
    Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. 
    Depois aplique o método adicione_juros() cinco vezes e imprime o saldo resultante.
'''
'''class contaInvestimento:
    def __init__(self,conta,nome,saldo,txJuros):
        self.txJuros = txJuros
        self.conta = conta
        self.nome = nome
        self.saldo = saldo
    def alterarNome(self,novoNome):
        self.nome = novoNome
    def deposito(self,valor):
        self.saldo += valor
    def saque(self,valor):
        if self.saldo>valor:
            self.saldo -= valor
        else:
            print('Saldo inferior ao valor do saque !')

    def adicionaJuros(self):
        self.saldo += (self.saldo*self.txJuros)/100

contInves = contaInvestimento('07225','Edson Tomas da Silva',1000,10)
contInves.adicionaJuros()
contInves.adicionaJuros()
contInves.adicionaJuros()
contInves.adicionaJuros()
contInves.adicionaJuros()
print(contInves.saldo)
'''
'''
5. Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
    - Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível 
    no tanque.

    - O consumo é especificado no construtor e o nível de combustível inicial é 0.

    - Forneça um método andar() que simule o ato de dirigir o veículo por uma certa distância, 
    reduzindo o nível de combustível no tanque de gasolina.
    - Forneça um método obter_gasolina(), que retorna o nível atual de combustível.
    - Forneça um método adicionar_gasolina(), para abastecer o tanque. Exemplo de uso:
    ```
    meu_carro = Carro(15);           # 15 quilômetros por litro de combustível. 
    meu_carro.adicionar_gasolina(20); # abastece com 20 litros de combustível. 
    meu_carro.andar(100);            # anda 100 quilômetros.
    meu_carro.obter_gasolina()        # Imprime o combustível que resta no tanque.
'''
'''class Carro:
    def __init__(self,consumo):
        self.consumo = consumo
        self.nivelComb = 0
    def abastecer(self,litros):
        self.nivelComb += litros
    def mostrarCombustivel(self):
        print(self.nivelComb)
    def andar(self,km):
        gastoComb = km/self.consumo
        self.nivelComb -= gastoComb

carro = Carro(15)
carro.abastecer(20)
carro.andar(100)
carro.mostrarCombustivel()'''

















    






    




