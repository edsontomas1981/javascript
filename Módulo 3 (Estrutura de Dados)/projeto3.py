from random import randint
class Ponteiro:
    def __init__ (self,vertice,coluna,matrix):
        self.vertice = vertice
        self.vertices = len(matrix)-1
        self.coluna = coluna
        self.colunas = len(matrix[0])-1
        self.visitados = [] 
        self.tamanho_rio = 0 
        self.rios = [] 

    def mover_esquerda(self):
        if self.coluna > 0:
            self.coluna -= 1
            return True
        else:
            return False
    def mover_cima(self):
        if self.vertice > 0:
            self.vertice -= 1
            return True
        else:
            return False

    def mover_baixo(self):
        if self.vertice < self.vertices:
            self.vertice += 1
            return True
        else :
            return False

    def mover_direita(self):
        if self.coluna < self.colunas:
            self.coluna += 1
            return True
        else:
            return False

    def marcar_visita(self):
        posicao = [self.vertice,self.coluna]
        self.visitados.append(posicao)

    def voltar(self,vertice,coluna):
        self.vertice = vertice
        self.coluna = coluna

class Matrix: #Classe para que as matrizes sejam geradas automaticamente
    def __init__(self):             
        vertices = randint(2,10)
        colunas = randint(2,10)
        self.vertices = vertices
        self.colunas = colunas
        self.vertice = []
        self.coluna = []

    def matriz(self):
        for iterador_vertices in range (self.vertices):
            self.coluna = []
            for iterador_colunas in range(self.colunas):
                item = randint(0,1)
                self.coluna.append(item)
            self.vertice.append(self.coluna)
        return self.vertice  

def proc_rio(vertice,coluna):
    ponteiro.vertice = vertice   
    ponteiro.coluna = coluna
    posicao = [vertice,coluna]
    if posicao not in ponteiro.visitados:
        ponteiro.marcar_visita()
        if matrix[ponteiro.vertice][ponteiro.coluna] == 1:
            ponteiro.tamanho_rio+=1
            if ponteiro.mover_direita():
                proc_rio(ponteiro.vertice,ponteiro.coluna)
                ponteiro.voltar(vertice,coluna)
            if ponteiro.mover_baixo():
                proc_rio(ponteiro.vertice,ponteiro.coluna)
                ponteiro.voltar(vertice,coluna)
            if ponteiro.mover_esquerda():
                proc_rio(ponteiro.vertice,ponteiro.coluna)
                ponteiro.voltar(vertice,coluna)
            if ponteiro.mover_cima():
                proc_rio(ponteiro.vertice,ponteiro.coluna)
                ponteiro.voltar(vertice,coluna)
        else:
            return
    else:
        return

gera_matriz = Matrix()
matrix = gera_matriz.matriz()
ponteiro = Ponteiro(0,0,matrix)

for vertice in range (len(matrix)):
    for coluna in range ((len(matrix[0]))):
        ponteiro.tamanho_rio = 0
        proc_rio(vertice,coluna)
        if ponteiro.tamanho_rio !=0:
            ponteiro.rios.append(ponteiro.tamanho_rio)

for i in matrix:
    print(i)

print('------------------------')   
print(ponteiro.rios)










            









 


