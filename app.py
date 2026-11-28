cores = {'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'limpa':'\033[m'
         }
print(f'{cores['vermelho']}={cores['limpa']}'*19)
print(f'{cores['vermelho']}AMBURGUERES DO JÃO{cores['limpa']}')
print(f'{cores['vermelho']}={cores['limpa']}'*19)
nome = input("Qual o seu nome?: ")
lanche = float(input('Quanto custou o lanche?: '))
bebida = float(input('Quanto custou a bebida?: '))
total = lanche + bebida
print(f'Olá, {nome}. O total da sua compra é {cores['amarelo']}R${total}{cores['limpa']}. Obrigado pela preferência!')
print(f'{cores['amarelo']}Bom lanche!{cores['limpa']}.')
