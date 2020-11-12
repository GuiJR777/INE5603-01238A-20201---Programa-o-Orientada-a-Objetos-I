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

def verifica(numero):
    numero = list(numero)
    digito = modulo_11(numero[:-1])
    if int(numero[-1]) == digito:
        resposta = True
    else:
        resposta = False

    return resposta

resposta = verifica(input())
print(resposta)