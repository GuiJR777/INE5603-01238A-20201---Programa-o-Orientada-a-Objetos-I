def decodificar(string):
    strings = string.split(' ')
    string_decode = []
    for str in strings:
        letras_p = list(str)
        letras = []
        for letra in letras_p[1::2]:
            letras.append(letra)
        new_str = ''.join(letras)
        string_decode.append(new_str)
        string_decode.append(' ')
    new_string = (''.join(string_decode)).lstrip()
    return new_string


resposta = decodificar(input())
print(resposta)

