def raiz_geo(n,input_list):
    produto = 1
    for i in input_list:
        produto = produto * i
    resultado = produto ** (1/n)

    return resultado

n = int(input(''))
valores = []
for i in range(n):
    v = int(input(''))
    valores.append(v)

resposta = round(raiz_geo(n, valores))

print(resposta)