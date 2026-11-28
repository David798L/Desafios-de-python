resp = ''

while resp != 'm' and resp != 'f':
    resp = input('Digite o sexo [M/F]: ').strip().lower()
    if resp != 'm' and resp != 'f':
        print('Opção inválida!')

print('Fim')