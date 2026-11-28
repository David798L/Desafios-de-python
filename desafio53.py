print('-'*10)
print('POLINDROMO')
print('-'*10)
frase1 = input('Digite uma frase: ').strip().lower()
frase2 = frase1[::-1]
if frase2 == frase1:
    print(f'A frase {frase1} é polindromo!')
else:
    print(f'A frase {frase1} não é polindromo!')
