# Entrada de dados
x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

# Computador o resultado
pode_moverse = False

if abs(x1-x2) == 2 and abs(y1-y2) == 1:
    pode_moverse = True
elif abs(x1-x2) == 1 and abs(y1-y2) == 2:
    pode_moverse = True

# Mostrar o resultado
print(pode_moverse)