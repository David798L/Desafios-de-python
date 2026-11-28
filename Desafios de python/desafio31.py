km = int(input('Digite a distancia da viagem em km/h: '))
if km <= 200:
    preç = km * 0.5
    print('O custo da viagem sera: {}R$'.format(preç))
else:
    preç = km * 0.45
    print('O custo da viagem sera: {}R$'.format(preç))
print('FIM')
