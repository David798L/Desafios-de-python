vel = int(input('Qual a velocidade do carro?:'))
if vel >= 80:
    vel = vel - 80
    mult = vel * 7
    print('Sua velocidade km/h passou {}km/h do limite e sua multa é {}R$'.format(vel, mult))
