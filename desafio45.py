import random
print('='*21)
print('PEDRA PAPEL E TESOURA')
print('='*21)
print(f'Escolha pedra, papel ou tesoura')
choice = ('pedra', 'papel', 'tesoura') 
player1 = str(input(': ')).lower()
player2 = random.choice(['pedra', 'papel', 'tesoura'])
print(f'Escolha do player2: {player2}')
if player1 == player2:
    print('Empate')
elif player1 == 'pedra' and player2 == 'tesoura':
    print('Vitoria do player1!')
elif player1 == 'tesoura' and player2 == 'papel':
    print('Vitoria do player1!')
elif player1 == 'papel' and player2 == 'pedra':
    print('Vitoria do player1!')
else:
    print('Vitoria do player2!')
  
