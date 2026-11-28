print('='*9)
print('TRIANGULO')
print('='*9)
r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As tres retas podem formar um triangulo!')
    if r1 == r2 == r3:
        print('E o triangulo é equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('E o triangulo é isóceles')
    else:
        print('E o triangulo é escaleno')
else:
    print('As tres retas não formam um triangulo!')
