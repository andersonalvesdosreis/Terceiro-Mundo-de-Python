matriz = [[], [], [], [], [], [], [], [], []]

contador_par = 0
soma_terceira_coluna = 0

for x in range(0, 9):
    pergunta = int(input('digite um valor: '))
    if pergunta %2 == 0:
        contador_par += pergunta
    matriz[x].append(pergunta)
    if x == 2 or x == 5 or x == 8:
        soma_terceira_coluna += pergunta

print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])
print('='*20)

segunda_linha = [ matriz[3] , matriz[4] , matriz[5] ]

print(f'A soma dos valores pares: {contador_par}')
print(f'O maior valor da segunda linha: {max(segunda_linha)}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print('='*20)
