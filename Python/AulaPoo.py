class Cadastro:
    #metodo contrutor
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
    
    #representação
    def __repr__(self):
        return f'Usuário {self.nome} email {self.email}'
    
usu1 = Cadastro('Edson','edson.transpioneira@gmail.com')

print(usu1)