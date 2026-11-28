print('PROGREÇÃO')
ptermo = 0
termos = 0
razao = 0
c = 0
resp = 's'
while resp == 's':
    ptermo = int(input('Digite o primeiro termo: '))
    termos = int(input('Digite quantos termos quer mostrar: '))
    razao = int(input('Digite a razao: '))
    for c in range(termos):
        print(f'{ptermo}', end=' ')
        ptermo = ptermo + razao
    print('| \n')
    resp = input('Quer continuar? [s/n]: ')

