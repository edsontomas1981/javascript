cpf=input("Digite o CPF : ")
cpf_lista=list(cpf) #transforma string em lista
cpf_multiplicador=[10,9,8,7,6,5,4,3,2]#gera os numeros a serem mutiplicados
primeiro_verificador = 0
segundo_verificador = 0

#calcula o 1º digito verificador
for cont in range(9):
    valor = int(cpf_lista[cont])*int(cpf_multiplicador[cont])
    primeiro_verificador += valor
primeiro_verificador = (primeiro_verificador*10)%11

#calcula o 2º digito verificador
cpf_multiplicador.insert(0,11)  
for cont in range(10):
    valor = int(cpf_lista[cont])*int(cpf_multiplicador[cont])
    segundo_verificador += valor
segundo_verificador = (segundo_verificador*10)%11


if (cpf_lista[9] == str(primeiro_verificador)) and (cpf_lista[10] == str(segundo_verificador)) :
    print(f"O CPF {cpf} é um cpf válido !")
else :
    print(f"O CPF {cpf} é um cpf inválido !")
