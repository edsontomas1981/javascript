import json
import os.path
import sys
def pegaDados():
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados
dados = pegaDados()
print(dados[0]['categoria'])

