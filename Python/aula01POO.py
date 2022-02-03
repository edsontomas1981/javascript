'''
Enunciado
Crie uma classe Funcionario cujos atributos são nome e e-mail. 
Guarde as horas trabalhadas em um dicionário cujas chaves são o mês em questão e, 
em outro dicionário, guarde o salário por hora relativo ao mês em questão. 
Crie um método que retorna o salário mensal do funcionário.
'''
class Funcionarios:
    
    def __init__ (self,nome,email):
        
        self.nome = nome
        self.email = email
        
    def HorasESalario (self,mes,horas,salario):
        self.mes = mes
        self.horaTrabalhadas = {mes:horas}
        self.salarioMes = {mes:salario}
    
    def CalculoSalarioMes(self):
        salario = self.horaTrabalhadas[self.mes] * self.salarioMes[self.mes]
        return salario
    
        
nome = input('Digite o nome do funcionario : ')
email = input('Digite o email funcionario : ')
funcionario=Funcionarios(nome,email)
funcMes = input('Digite o mes : ')
funcHoras  = float(input('Digite as horas trabalhadas : '))
funcSalario  = float(input('Digite 0 salário por hora : '))

funcionario.HorasESalario(funcMes,funcHoras,funcSalario)
print(funcionario.CalculoSalarioMes())