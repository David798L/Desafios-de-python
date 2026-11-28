print('='*23)
print('PROGRESSÃO ARITIMETICA')
print('='*23)
prime = int(input('Digite o primeiro: '))
razao = int(input('Digite a razao: '))
for c in range (0, 10):
    termo = prime + (c * razao)
    print(f'{termo}', end='')
