print('-'*12)
print('NUMERO PRIMO')
print('-'*12)
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot = tot + 1
if tot == 2:
    print('O numero é primo!')
else:
    print('O numero não é primo!')