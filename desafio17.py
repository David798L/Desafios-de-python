from math import hypot
cateto1 = int(input('digite o seno: '))
cateto2 = int(input('digite o cosseno: '))
hipo = hypot(cateto1, cateto2)
print('a hipotenusa do seno {} e do cosseno {} é {:.1f}.'.format(cateto1, cateto2, hipo))
