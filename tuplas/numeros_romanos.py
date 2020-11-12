def converte(numero_romano):
    romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    numero_romano = list(numero_romano)
    numero_romano.reverse()
    numero_convertido = 0
    ultimo = int(romanos[numero_romano[0]])
    for str in numero_romano:
        numero = int(romanos[str])
        if numero >= ultimo:
            numero_convertido = numero_convertido + numero
        elif numero < ultimo:
            numero_convertido = numero_convertido - numero
        ultimo = numero

    return numero_convertido

resposta = converte(input())
print(resposta)
