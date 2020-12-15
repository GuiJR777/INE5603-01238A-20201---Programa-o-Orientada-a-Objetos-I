# Funções
def traduzir(frase, dicionario):
    '''
        param frase: Recebe a frase a ser traduzida em formato string
        param dicionario: Recebe o dicionario de palavras a serem traduzidas
        return: Retorna a frase recebida traduzida de acordo com o dicionario
    '''
    for key in dicionario:
        frase = str(frase).replace(key, dicionario[key])
    return frase

# Recebendo os dados
t = int(input(''))
dic = {}
letra_japones = []
letra_traduzida = []

# Processando
for instancia in range(t):
    entrada = str(input('')).split(' ')
    m = int(entrada[0])
    n = int(entrada[1])
    for palavras in range(m):
        if m != 0:
            key = input('')
            value = input('')
            dic[key] = value
    for frases in range(n):
        frase = input('')
        letra_japones.append(frase)
    letra_japones.append('') #Apenas para deixar uma linha em branco entre as instancias

# Resultado
for frase in letra_japones:
    traducao = traduzir(frase, dic)
    print(traducao)


