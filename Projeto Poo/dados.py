import json
import os.path
import sys


class Dados:
    def obtemDados():
        with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
            dados = json.loads(arq.read())
        return dados
    