nome = input('Digite o nome: ').lower()
print('A letra A aparece {} vezes'.format(nome.count('a')))
print('A letra A apareceu pela primeira vez na posição {}'.format(nome.find('a')))
print('A letra A apareceu pela ultima vez na posição {}'.format(nome.rfind('a')))
