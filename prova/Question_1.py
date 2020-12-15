# Funções
def lista_coluna(coluna, matriz):
    '''
        param coluna: Recebe valor da coluna atual
        param matriz: Recebe a matriz
        return: Retorna uma lista contendo os valores da coluna analisada
    '''
    lista = []
    for linha in matriz:
        lista.append(linha[coluna])
    return lista

def confere_linha(numero, linha):
    '''
        param numero: Recebe valor que esta sob analise
        param linha: Recebe a lista com valores da linha que esta sob analise
        return: Retorna um booleano que indicca se o numero é o menor de sua linha
    '''
    resposta = True
    for i in linha:
        if numero <= int(i) and numero >= 1:
            pass
        else:
            resposta = False
    return resposta

def confere_coluna(numero, coluna):
    '''
        param numero: Recebe valor que esta sob analise
        param linha: Recebe a lista de valores da coluna que esta sob analise
        return: Retorna um booleano que indicca se o numero é o maior de sua coluna
    '''
    resposta = True
    for i in coluna:
        if numero >= int(i) and numero >= 1:
            pass
        else:
            resposta = False
    return resposta

# Recebendo os dados
entrada = input('').split(' ')
n = int(entrada[0])
m = int(entrada[1])
matriz = []
for i in range(n):
    linha = input('').split(' ')
    matriz.append(linha)
resposta = False

# Processando
contador_i = 0
for i in matriz:
    contador_j = 0
    for j in i:
        j = int(j)
        menor = confere_linha(j, i)
        if menor:
            coluna = lista_coluna(contador_j, matriz)
            maior = confere_coluna(j, coluna)
            if maior:
                resposta = '{} {}'.format(contador_i+1, contador_j+1)
        contador_j+=1
    contador_i+=1

print(resposta)