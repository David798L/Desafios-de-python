cores = {'verde':'\033[32m',
         'limpa':'\033[m'
         }
print(f'{cores['verde']}={cores['limpa']}'*23)
print(f'{cores['verde']}| ALISTAMENTO MILITAR |{cores['limpa']}')
print(f'{cores['verde']}={cores['limpa']}'*23)
anon = int(input('Digite o ano de nascimento: '))
anoa = int(input('Digite o ano atual: '))
idade = anoa - anon
if idade >= 17 and idade <= 18:
    print('-'*24)
    print('Ja se alistou? [SIM/NÃO]')
    print('-'*24)
    resp = input(': ').lower()
    if resp == 'sim':
        print('Se você ja se alistou, compareça ao exercito da sua regia na hora e dia designados!')
    elif resp == 'nao':
        print('Se você ainda não se alistou, alistesse o mais rapido o possivel e siga as instruçoes do alistamento!')
elif idade > 18:
    print('-'*24)
    print('Ja se alistou? [SIM/NÃO]')
    print('-'*24)
    resp = input(': ').lower() 
    if resp == 'sim':
        print('Você ja se alistou, foi dispensado ou serviu!')  
    elif resp == 'nao':
        print('Você não se alistou e esta atrasado, va a junta de sua regiao e pague a multa de 6.38R$!')
elif idade < 17:
    idade = 18 - idade
    print(f'Você ainda não esta em idade de alistamento, faltam {idade} anos para seu alistamento')
print('FIM')
    