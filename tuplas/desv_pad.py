def media_simples(valores):
    soma = 0
    for n in valores:
        soma = soma + n
    media = soma/(len(valores))
    return media

def somatorio_dist(valores, media):
    somatorio = 0
    for i in valores:
        dist = (i - media)**2
        somatorio = somatorio + dist
    return somatorio


def dp(n, valores):
    media = media_simples(valores)
    dist = somatorio_dist(valores, media)
    next = dist / (len(valores)-1)
    desv_pad = next**(1/2)
    return desv_pad

n = int(input(''))
valores = []
for i in range(n):
    v = float(input(''))
    valores.append(v)

resposta = dp(n, valores)
print(resposta)

