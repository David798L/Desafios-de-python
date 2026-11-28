print('-'*26)
print('|INDECE DE MASSA CORPOREA|')
print('-'*26)
peso = float(input('Digite o peso: '))
altu = float(input('Digite a altura: ').replace(',', '.'))
imc = peso / (altu ** 2)
if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc <= 24.99:
    print('Peso ideal')
elif imc >= 25 and imc <= 29.99:
    print('Acima do pes')
elif imc >= 30 and imc <= 39.99:
    print('Obesidade')
else:
    print('Obesidade morbida')
print('FIM')
