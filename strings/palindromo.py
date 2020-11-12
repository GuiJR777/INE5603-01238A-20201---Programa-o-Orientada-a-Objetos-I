# Verificador
def higienizador(string):
    string = string.lower()
    string = string.replace(' ','')
    string = string.replace(',','')
    string = string.replace('-','')
    return string

def verifica_palindromo(string):
    palavra = higienizador(string)
    resposta = True
    counter = 1
    for letra in palavra:
        if letra == palavra[-counter]:
            counter += 1
        else:
            resposta = False
    return resposta

# Recebe dados
palavra = input()

# Resultado
resposta = verifica_palindromo(palavra)
print(resposta)

        

    