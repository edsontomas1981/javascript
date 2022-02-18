import platform
#import clientes
#import lojas
#import estoque
import os
print(platform.system())
print(platform.release())

def limpaTela():
    so = platform.system()
    if so == 'Linux':
        os.system('clear')
    
print('--------------------------------------------------------')    
limpaTela()
    

