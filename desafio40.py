cores = {'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'limpa':'\033[m'
         }
print('='*5)
print('MEDIA')
print('='*5)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'O aluno esta {cores['vermelho']}REPROVADO!{cores['limpa']}')
elif media >= 5.0 and media <= 6.9:
    print(f'O aluno esta na {cores['amarelo']}RECUPERAÇÃO!{cores['limpa']}')
elif media >= 7.0:
    print(f'O aluno {cores['verde']}PASSOU!{cores['limpa']}')
