# Funções
def contador_vitorias(numero_jogadas):
    for i in range(numero_jogadas):
        jogadas = input()
        jogadas = list(jogadas)
        vitorias = {'John': 0, 'Mary': 0}
        for j in jogadas:
            if j == '1':
                vitorias['John'] = int(vitorias['John']) + 1
            elif j == '0':
                vitorias['Mary'] = int(vitorias['Mary']) + 1
        return vitorias

for i in range(2):
    vitorias = contador_vitorias(int(input()))
    print('Mary won {} times and John won {} times'.format(vitorias['Mary'], vitorias['John']))
