cores =  {'azul':'\033[34m',
          'amarelo':'\033[33m',
          'limpa':'\033[m'}
print(f'{cores['azul']}-{cores['limpa']}'*25)
print(f'{cores['azul']}BINARIO.OCTAL.HEXADECIMAL{cores['limpa']}')
print(f'{cores['azul']}-{cores['limpa']}'*25)
num = int(input('Digite o numero que deseja converter: '))
print(f'Digite [1] para {cores['amarelo']}BINARIO{cores['limpa']}')
print(f'Digite [2] para {cores['amarelo']}OCTAL{cores['limpa']}')
print(f'Digite [3] para {cores['amarelo']}HEXADECIMAL{cores['limpa']}')
resp = int(input(': '))
if resp == 1:
    num = bin(num)
    print(f'O numero convertido para decimal é: {num[2:]}')
elif resp == 2:
    num = oct(num)
    print(f'O nunero convertido para octal é: {num[2:]}')
elif resp == 3:
    num = hex(num)
    print(f'O numero convertido para hexadecimal é: {num[2:]}')
print('FIM')
