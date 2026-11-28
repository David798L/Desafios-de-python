cores = {'verde':'\033[32;47m',
         'limpa':'\033[m'
         }
print(f'{cores['verde']}={cores['limpa']}'*21)
print(f'{cores['verde']}ANTECESSOR E SUCESSOR{cores['limpa']}')
print(f'{cores['verde']}={cores['limpa']}'*21)
n = int(input('Digite um numero: '))
s = n + 1
a = n - 1
print(f'o numero é {n} o antecessor é {a} e o sucessor é {s}')
print('FIM')
