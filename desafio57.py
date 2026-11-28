print('='*14)
print('LEITOR DE SEXO')
print('='*14)
resp = ' '
while resp not in ('m', 'f'):
    resp = input('Digite o sexo[M/F]: ')
    if resp not in ('m', 'f'):
        print('resposta invalida!')
print('fim')
      