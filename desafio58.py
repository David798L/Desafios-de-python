import random
print('='*11)
print('ADIVINHAÇÃO')
print('='*11)
resp = 0
tentativas = 0
computador = random.randint(1, 10)
while resp != computador:
    resp = int(input('Digite a sua escolha: '))
    tentativas = tentativas + 1
    if resp != computador:
        print('Errado, tente denovo') 
print(
    f'Correto!, mas voce precisou de {tentativas} tentativas\n'
    f'FIM'
      )
