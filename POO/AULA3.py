'''import time
import os
class Cronometro:
    def __init__(self,horas,minutos,segundos):
        self.hora=horas
        self.minutos = minutos
        self.segundos = segundos
    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}{self.segundos:02d}'
    def incremento(self):
        if self.segundos> 60:
            self.segundos = 0
            self.minutos +=1
        if self.minutos > 60:
            self.minutos = 0
            self.horas += 1
        self.segundos += 1
    
    def start(self):
        while True :
            print(self)
            self.incremento()
            '''
from re import S


class Funcionarios:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario = {}
    def horasMes(self,mes,horas):
        self.horas.append({mes:horas})
        print(self.horas)
    def salarioMes (self,mes,salario):
        self.salario.append({mes:salario})
        print(self.salario)
    def __repr__(self):
        return f'{self.nome} {self.horas} {self.salario} '

cond = input('Deseja Incluir ? ')
nome = 'edson'
email = "edson@edson"
func = Funcionarios(nome,email)
while cond == 's':
    mes = input('competencia')
    horas = input('horas')
    salario = input('salario')
    func.horasMes(mes,horas)
    func.salarioMes(mes,salario)
    cond = input('Deseja Incluir ? ')
print(func)




