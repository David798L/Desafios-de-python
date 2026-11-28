sal = int(input('Digite o salario: '))
if sal >= 1250:
    sal = (sal * 0.10) + sal
    print('O aumento de salario sera 10%, ficando {}'.format(sal))
else:
    sal = (sal * 0.15) + sal
    print('O aumento de salario sera 15%, ficando {}'.format(sal))
