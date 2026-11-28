cores = {'azul':'\033[34m',
         'linha':'\033[4m',
         'limpa':'\033[m'
         }
print('='*4)
print(f'{cores['azul']}SOMA{cores['limpa']}')
print('='*4)
numero1 = int(input('Primeiro numero: '))
numero2 = int(input('Segundo numero: '))
soma = numero1 + numero2
print(f'a soma entre {numero1} e {numero2} vale {cores['linha']}{soma}{cores['limpa']}')
print('FIM')
