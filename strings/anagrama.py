# Verificador
def verifica_anagrama(string1, string2):
    resposta = True
    palavra1 = []
    palavra2 = []
    if string1 == string2:
        resposta = False
    else:
        for letra in string1:
            palavra1.append(letra)
        for letra in string2:
            palavra2.append(letra)
        if len(palavra1) == len(palavra2):
            for letra in palavra1:
                if letra in palavra2:
                    palavra2.remove(letra)
                else:
                    resposta = False
        else:
            resposta = False

    return resposta


# Coleta dados
string1 = input()
string2 = input()

# Resultado
resposta = verifica_anagrama(string1, string2)
print(resposta)