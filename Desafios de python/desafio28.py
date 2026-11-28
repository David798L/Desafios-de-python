import random
n1 = random.randint(1, 6)
n2 = int(input('Adivinhe um numero: '))
if n1 == n2:
    print('\033[1;32mAcertou!\033[m O numero era {}'.format(n1))
else:
    print('\033[1;31mEscolha errada!\033[m O numero era {}'.format(n1))
print('\033[0mFIM')
