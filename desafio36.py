cores = {'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'limpa':'\033[m'
         }
print(f'{cores['amarelo']}={cores['limpa']}'*21)
print(f'{cores['amarelo']}EMPRESIMO RESIDENCIAL{cores['limpa']}')
print(f'{cores['amarelo']}={cores['limpa']}'*21)
valor = int(input(f'Digite o valor do imovel em {cores['amarelo']}R${cores['limpa']}: '))
salio = int(input(f'Digite o salario em {cores['amarelo']}R${cores['limpa']} do comprador: '))
ano = int(input('Quer pagar em quantos anos?: '))
prest = valor / (ano * 12)
print(f'O valor da prestação será {prest:.2f}{cores['amarelo']}R${cores['limpa']}' )
if prest > salio * 0.30:
    print(f'Emprestimo {cores['vermelho']}NEGADO!{cores['limpa']}')
elif prest <= salio * 0.30:
    print(f'Emprestimo {cores['verde']}LIBERADO!{cores['limpa']}')
