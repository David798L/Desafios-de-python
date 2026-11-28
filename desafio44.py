print('='*14)
print('MERCADO CORREA')
print('='*14)
preço = float(input('Digite o preço dos produtos: '))
print(
    f'Modos de pagamento:\n'
    f'1: [CHEQUE/DINHEIRO]: 10% de desconto\n'
    f'2: [A VISTA NO CARTÃO]: 5% de desconto\n'
    f'3: [ATE 2X NO CARTAO]: preço padrao\n'
    f'4: [3X OU MAIS NO CARTÃO]: 20% de juro'
)
modop = int(input('Escolha o modo de pagamento: '))
if modop == 1:
    preço = preço - preço * 0.10
    print(f'O preço no modo CHEQUE/DINHEIRO fica {preço}')
elif modop == 2:
    preço = preço - preço * 0.05
    print(f'O preço no modo [A VISTA NO CARTÃO] fica {preço}')
elif modop == 3:
    print(f'O preço no modo [ATE 2X NO CARTAO] fica {preço}')
elif modop == 4:
    preço = preço + preço * 0.20
    print(f'O preço no modo [3X OU MAIS NO CARTAO] fica {preço}')
else:
    print('Opção de pagamento invalida!')
    