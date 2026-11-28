from datetime import date
print('MAIORIDADE') 
mai = 0
men = 0
atual = date.today().year
for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = atual - ano
    if idade >= 18:
       mai = mai + 1
    else:
       men = men + 1
print(f'Das sete pessoas, {mai} são maiores de idade e {men} são menores')
