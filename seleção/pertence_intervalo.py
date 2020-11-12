'''
Verificar se um determinado valor x (inteiro) pertence ao intervalo fechado [a..b]. 
Na entrada, os valores estão nesta ordem: x, a, b. 
O resultado é um valor lógico true ou false.

Exemplo de entrada:
    15
    3
    18
Saída:
    true

'''
#Comparador
def verifica_intervalo(x, a, b):
    if x >= a and x <= b:
        resposta = True
    else:
        resposta = False
    return resposta

#Recebendo dados
x = int(input())
a = int(input())
b = int(input())

#Resultado
resultado = verifica_intervalo(x, a, b)
print(resultado)
  
