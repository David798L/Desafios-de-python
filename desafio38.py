cores = {'amarelo':'\033[33m',
         'limpa':'\033[m'
         }
print(f'{cores['amarelo']}={cores['limpa']}'*22)
print(f'{cores['amarelo']}MENOR, MAIOR OU IGUAL?{cores['limpa']}')
print(f'{cores['amarelo']}={cores['limpa']}'*22)
num1 = float(input('Digite o primeiro numero desejado: '))
num2 = float(input('Digite o segundo numero desejado: '))
if num1 > num2:
    print('O primeiro numero é maior!')
elif num2 > num1:
    print('O segundo numero é maior!')
else:
    print('Os numeros são iguais')
