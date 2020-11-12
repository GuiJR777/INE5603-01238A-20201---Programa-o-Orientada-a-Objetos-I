# Funções
def higienizador(string):
    string = string.lower()
    string = string.replace(' ','')
    string = string.replace(',','')
    string = string.replace('-','')
    string = string.replace('.','')
    return string

def checa_igualdade(lista):
    repetidos = 0
    for n in range(len(lista)):
        if lista[0] == lista[n]:
            repetidos+=1
        else:
            pass
    if repetidos >= len(lista):
        resposta = True
    else:
        resposta = False
    return resposta


def modulo_11(numero):
    numero.reverse()
    soma = 0
    peso = 2
    for n in numero:
        soma = soma + (int(n)*peso)
        peso += 1
    resto = soma % 11
    if resto > 11:
        dv = resto - 11
    else:
        dv = 11 - resto
    if dv >= 10:
        dv = 0
    
    return dv

def verifica_digito(cpf):
    todos_numeros = list(cpf)
    nove_numeros = []
    dois_ultimos = []
    if len(todos_numeros) != 11:
        resposta = False
    else:
        igual = checa_igualdade(todos_numeros)
        if igual == True:
            resposta = False
        else:
            for i in range(9):
                nove_numeros.append(todos_numeros[i])
            dois_ultimos.append(todos_numeros[9::])
            dois_ultimos = f'{dois_ultimos[0][0]}{dois_ultimos[0][1]}'
            primeiro_digito = modulo_11(nove_numeros)
            nove_numeros.reverse()
            nove_numeros.append(primeiro_digito)
            segundo_digito = modulo_11(nove_numeros)
            digito_validador = f'{primeiro_digito}{segundo_digito}'
            if digito_validador == dois_ultimos:
                resposta = True
            else:
                resposta = False
    return resposta

cpf = higienizador(input())
resposta = verifica_digito(cpf)
print(resposta)
