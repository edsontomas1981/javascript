import json
import os.path
import sys
from operator import itemgetter

def ordenaLista(dados:list):
    listaPrecoFloat = []
    for lista in dados:
        listaPrecoFloat.append({'id':lista['id'],
                                'preco':float(lista['preco']),
                                'categoria':lista['categoria']
                                })
    listaOrdenada = sorted(listaPrecoFloat,key=itemgetter('preco'))
    return listaOrdenada
def imprimi_menu () :
    os.system('clear')
    print(letraCores.AZUL+"Escolha uma opção : "+letraCores.AMARELO)
    print("1. Listar categorias :")
    print("2. Listar produtos de uma categoria :")
    print("3. Produto mais caro por categoria :")
    print("4. Produto mais barato por categoria :")
    print("5. Top 10 produtos mais caros :")
    print("6. Top 10 produtos mais baratos :")
    print("0. Sair :"+letraCores.BRANCO)
    opcao = input(letraCores.VERDE+"Digite a opção desejada : "+letraCores.BRANCO)
    if opcao.isdigit():
        return int(opcao)
    else:
        print('Opçao inválida !')
        return 7
class letraCores:
    VERDE = '\033[92m' 
    AMARELO = '\033[93m' 
    VERMELHO = '\033[91m' 
    AZUL = '\033[94m' 
    BRANCO = '\033[0m' 
def voltaMenu():

    print(letraCores.AMARELO+"Deseja voltar ao menu inicial ?"+letraCores.BRANCO)
    opcao=input("Digite 9 para retornar ou qualquer tecla para sair : ")    
    if opcao == '9' :
        menu(d)
    else:
        os.system('clear')
        print("Finalizando ....  ")
def verificaCategoriaExiste(dados,categoria):
    categoriaExiste = False
    for elemento in dados:
        if elemento['categoria'] == categoria:
            categoriaExiste = True
    return categoriaExiste

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    lista = []
    for cont in range (len(dados)):
        catego = dados[cont]['categoria']
        if catego not in lista :
            lista.append(dados[cont]['categoria'])
    return lista   

def produto_mais_barato(dados, categoria):
    produtos=listar_por_categoria(dados,categoria)
    valor=float(produtos[0]['preco'])
    preco=999999
    produtoMaisBarato = {}
    for produto in produtos:
        preco = float(produto['preco'])
        if valor > preco :
            valor=float(produto['preco'])
            produtoMaisBarato = produto
    return produtoMaisBarato

def produto_mais_caro(dados, categoria):
    produtos=listar_por_categoria(dados,categoria)
    produtoMaisCaro = {}
    valor=float(produtos[0]['preco'])
    preco=0
    for produto in produtos:
        preco = float(produto['preco'])
        if valor < preco :
            valor=float(produto['preco'])
            produtoMaisCaro = produto
    return produtoMaisCaro

def listar_por_categoria(dados, categoria):
    prod_por_categoria =[]
    for prod in dados:
        if prod['categoria'] == categoria:
            prod_por_categoria.append(prod)
    return prod_por_categoria

def top_10_caros(dados):
    lista = ordenaLista(dados)
    lista = sorted(lista, key=itemgetter('preco'),reverse=True)
    topMaisCaros = []
    for cont in range (10):
        topMaisCaros.append(lista[cont])
    return topMaisCaros

def top_10_baratos(dados):
    lista = ordenaLista(dados)
    topMaisBaratos = []
    for cont in range (10):
        topMaisBaratos.append(lista[cont])
    return topMaisBaratos

def menu(dados):
    opcao = imprimi_menu()
    while opcao > 6 or opcao < 0:
        print(letraCores.VERMELHO +"Opção inválida" + letraCores.BRANCO )
        opcao=imprimi_menu()
    if opcao == 1:
        dados = []
        categorias=listar_categorias(d)
        for lista_imp_categorias in categorias:
            print(lista_imp_categorias)
        voltaMenu()
    elif opcao == 2:
        categoria=input('Digite a categoria desejada : ')
        categoriaExiste = verificaCategoriaExiste(d,categoria)
        if categoriaExiste :
            prod_por_categ = listar_por_categoria(d,categoria)
            for prod in prod_por_categ:
                produto,preco,categ = prod.values()
                print(f'Produto : {produto} | Categoria : {categ} | Valor R$ {preco} ')
        else:
            print('Categoria não encontrada')
        voltaMenu()
    elif opcao == 3:
        dados=d
        categoria=input('Digite a categoria desejada : ')
        categoriaExiste = verificaCategoriaExiste(d,categoria)
        if categoriaExiste :
            prod_mais_caro=produto_mais_caro(d,categoria)
            produto,preco,categoria = prod_mais_caro.values()
            print(f'{letraCores.AZUL}O produto mais caro da Categoria {categoria} é {produto} custando{letraCores.VERMELHO} R${preco}{letraCores.BRANCO} ' )
        else:
            print('Categoria não encontrada !')
        voltaMenu()
    elif opcao == 4:
        dados=d
        categoria=input('Digite a categoria desejada : ')
        categoriaExiste = verificaCategoriaExiste(d,categoria)
        if categoriaExiste :
            prod_mais_barato=produto_mais_barato(d,categoria)
            produto,preco,categoria = prod_mais_barato.values()
            print(f'{letraCores.AMARELO}O produto mais barato da categoria {categoria} é {produto} custando{letraCores.AZUL} R${preco}{letraCores.BRANCO} ' )
        else:
            print('Categoria não encontrada')
        voltaMenu()

    elif opcao == 5 :
        dados = d
        listaProd = top_10_caros(dados)
        print('Os 10 produtos mais caros são : ')
        i = 1
        for prod in listaProd:
            produto,preco,categoria = prod.values()
            print(f'{i}º Id do produto : {produto} | Categoria {categoria} |{letraCores.VERMELHO} Preço {preco} {letraCores.BRANCO} ')
            i+=1
        voltaMenu()
    elif opcao == 6 :
        dados = d
        listaProd = top_10_baratos(dados)
        print('Os 10 produtos mais Baratos são : ')
        i = 1
        for prod in listaProd:
            produto,preco,categoria = prod.values()
            print(f'{i}º Id do produto : {produto} | Categoria {categoria} |{letraCores.AMARELO} Preço {preco} {letraCores.BRANCO}')
            i+=1
        voltaMenu()  
    
    elif opcao == 7 :
        print('Opção inválida !')
        imprimi_menu()
    
    else :
        os.system('clear')
        print('Finalizando ')

d = obter_dados()
menu(d)










