print('='*8)
print('CAUCULOS')
print('='*8)
escolha = ' '
escolhan = 0
resp = ' '
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
while resp != 5:
    print(
    f'Para somar [1]\n'
    f'Para multiplicar [2]\n'
    f'Para maior [3]\n'
    f'Para novos numeros [4]\n'
    f'Para fechar [5]'
    )
    resp = int(input('Digite sua resposta: '))
    if resp == 1:
        print(f'A soma de {n1} e {n2} é {n1 + n2}')
    elif resp == 2:
        print(f' A multiplicação de {n1} x {n2} é {n1 * n2}')
    elif resp == 3:
        if n1 > n2:
            print(f'O maior é : {n1}')
        elif n2 > n1:
            print(f'O maior é : {n2}')
        else:
            print('Os numeros são iguais!')
    elif resp == 4:
        while escolha != 'n':
            escolhan = int(input('Qual numero quer mudar?[1/2]: '))
            if escolhan == 1:
                n1 = int(input('Digite sua escolha: '))
            elif escolhan == 2:
                n2 = int(input('Digite sua escolha: '))
            else:
                print('Escolha invalida')
            escolha = input('Quer mudar algum numero?[n/s]: ')
    elif resp == 5:
        print('Fechamento...')
    else:
        print('Resposta invalida')
    escolha = ' '
