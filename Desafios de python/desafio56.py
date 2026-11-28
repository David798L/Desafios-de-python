print('CLASSIFICADOR')
grupo = 0
mulheres = 0
idade2 = 0
nomev = ' '
for c in range(0, 4):
    nome = input('Digite o nome: ')
    sexo = input(f'Digite o sexo de [{nome}]: ').lower()
    idade = int(input(F'Digite a idade de [{nome}]: '))
    if idade > idade2 and sexo == 'masculino':
       idade2 = idade
       nomev = nome
    if idade <= 20 and sexo == 'feminino':
       mulheres = mulheres + 1 
    grupo = grupo + idade
grupo = grupo / 4
print(
   f'O homen mais velho do grupo é {nomev}\n'
   f'Existem mulheres {mulheres} com menos de 20 anos no grupo\n'
   f'A media de idade do grupo é : {grupo}'
   )
