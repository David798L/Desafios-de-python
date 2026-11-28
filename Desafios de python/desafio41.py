print('-'*32)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-'*32)
idade = int(input('Digite a idade do atleta: '))
if idade < 14:
    print('O atleta esta na categoria mirim!')
elif idade >= 14 and idade < 19:
    print('O atleta esta na categoria infantil!')
elif idade >= 19 and idade < 20:
    print('O atleta esta na categoria junior!')
elif idade == 20:
    print('O atleta esta na categoria senior!')
elif idade > 20:
    print('O atleta esta na categoria master!')
print('FIM')
