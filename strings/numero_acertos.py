# Funções
def verifica_gabarito(prova , gabarito):
    respostas_aluno = list(prova)
    respostas_corretas = list(gabarito)
    acertos = 0
    for i in range(len(respostas_aluno)):
        if respostas_aluno[i] == respostas_corretas[i]:
            acertos += 1
        else:
            pass
    return acertos

# Execução
resposta = verifica_gabarito(input(),input())
print(resposta)
