# Funções
def conta_maria(numero_nomes):
    contador = 0
    for i in range(numero_nomes):
        nome = input()
        nome = nome.split(' ')
        if 'Maria' in nome:
            contador += 1
        else:
            pass
    return contador

resposta = conta_maria(int(input()))
print(resposta) 