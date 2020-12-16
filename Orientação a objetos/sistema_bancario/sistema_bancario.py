from banco import Banco

bc = Banco("Banco do Brejo", 999)

comandos = []
for i in range(7):
    comando = input('').split(' ')
    comandos.append(comando)

cc = {}
cpfs = []
contador = 1
for comando in comandos:
    if comando[0] == 'abre_conta':
        bc.abre_conta(comando[2], comando[1])
        cc[comando[1]] = contador
        cpfs.append(comando[1])
        contador+=1
    elif comando[0] == 'deposito':
        bc.deposito(cc[comando[1]], float(comando[2]))
    elif comando[0] == 'transferencia':
        bc.transferencia(cc[comando[1]], cc[comando[2]], float(comando[3]))
    elif comando[0] == 'saque':
        bc.saque(cc[comando[1]], float(comando[2]))

cpfs.sort(key=int)

# nj = bc.abre_conta("Joãozinho", 23456)
# nm = bc.abre_conta("Mariazinha", 123456)
# bc.deposito(nj, 100)
# bc.deposito(nm, 250)
# bc.saque(nj, 50)
# bc.transferencia(nm, nj, 20)

for cpf in cpfs:
    print('{} {}'.format(cpf, bc.saldo(cc[cpf])))
