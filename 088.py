import random
print('-'*20)
print(' '*5,'Jogo da mega Sena',' '*5)
print('-'*20)

n = int(input('Quantos jogos você deseja? '))
print(f'Sorteando {n} Jogos!')

for num in range(1,n+1):
    numeros = random.sample(range(1, 60), 6)
    numeros.sort()
    print(f'O Jogo{num}: {numeros}')

print('Boa Sorte!')
