altura = float(input('Qual a altura da parede?: '))
largura = float(input('Qual a largura da parede?: '))
area = altura * largura
tinta = area / 2
print('A parede tem {:.1f}m de altura, {:.1f}m de largura e {:.1f} de area, sera nescessario {:.1f}l de tinta para a pintura'.format(altura, largura, area, tinta))
