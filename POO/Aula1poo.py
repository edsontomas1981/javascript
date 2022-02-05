
import math
pi = math.pi

'''class Bola:

    def __init__(self,cor,raio):

        self.cor=cor #
        self.raio=raio

    def ImprimiCor(self):
        
        print(f'A cor da bola é {self.cor} ')

    def Area(self):
        
        area = (4*pi)*(self.raio ** 2)
        return area

    def Volume (self):
        volume = (4*pi)*(self.raio ** 3)/3
        return volume
bola=Bola("azul",2)
bola.ImprimiCor()
print(f'A área da bola é ; {bola.Area()}')
print(f'O volume da bola é ; {bola.Volume()}')'''

'''
Enunciado
Crie uma classe Retângulo cujos atributos são lado_a e lado_b. 
Crie um método para calcular a área desse retângulo. 
Crie um objeto dessa classe e calcule a área e a imprima em seguida.
'''

'''class Retangulo:

    def __init__(self,ladoA,ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    def Area (self):
        area = self.ladoA * self.ladoB
        return area

retangulo=Retangulo(3,3)
print(f'A área do retangulo é : {retangulo.Area()}')'''

class Televisor:
    def __init__(self,fabricante,modelo,canalAtual,listaDeCanais:list,volume):
        
        self.fabricante = fabricante
        self.modelo = modelo
        self.canalAtual = canalAtual
        self.listaDeCanais = listaDeCanais
        self.volume = volume
    
    def abaixaVolume (self):
    
        if self.volume > 0 :
            self.volume -= 1
        
    def aumentaVolume(self):
        if self.volume <= 100:
            self.volume +=1

cont = 's'
listaCanal = []
while cont != 'n':
    numeroCanal = input('Digite o numero do canal : ')
    nomeCanal = input('Digite o nome do canal : ')
    if numeroCanal not in listaCanal:
        listaCanal.append({numeroCanal:nomeCanal})
        cont = input('deseja continuar s/n :')
    else:
        print('canal já adicionado')
        cont = input('deseja continuar s/n :')

print(listaCanal)




   
        



    


