def checa_primeira_letra(lista):
    primeira_palavra = list(lista[0])
    primeira_letra = primeira_palavra[0]
    return primeira_letra

def checa_tautograma(frase):
    frase = frase.lower()
    tauto = True
    strings = frase.split(' ')
    primeira_letra = checa_primeira_letra(strings)
    for string in strings:
        if string[0] == primeira_letra:
            pass
        else:
            tauto = False
    return tauto

string = None
while string != '*':
    string = input()
    if string == '*':
        pass
    else:
        resposta = checa_tautograma(string)
        if resposta == True:
            print('Y')
        else:
            print('N')