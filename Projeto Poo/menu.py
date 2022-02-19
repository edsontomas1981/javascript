import lojas
import clientes
listaClientes=[]
def criaLoja():
    loja = lojas.Loja()

def criaCliente(nome,tipoAluguel,tempoAluguel):
    nome=clientes.Cliente(nome,tipoAluguel,tempoAluguel)
    listaClientes.append(nome)
loja=criaLoja()
criaCliente('Edson',1,5)
criaCliente('Sandra',2,2)
criaCliente('Ana',3,1)
print(listaClientes)
