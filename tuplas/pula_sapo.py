def jump(altura_atual, pulo, cano):
    altura_max = altura_atual + pulo
    altura_min = altura_atual - pulo
    if altura_max < cano or altura_min > cano:
        result = False
    else:
        result = True
    return result

entrada = input('').split(' ')
p = int(entrada[0])
numero_canos = int(entrada[1])
altura_canos = input('').split(' ')
altura_atual = 0
resultado = 'YOU WIN'

for cano in altura_canos:
    result = jump(altura_atual, p, int(cano))
    altura_atual = altura_atual + int(cano)
    if result == False:
        resultado = 'GAME OVER'
    else:
        pass

print(resultado)