primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))
quarto = int(input('Digite o quarto valor: '))

tupla = (primeiro, segundo, terceiro, quarto)
print(f'Os valores digitados foram {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

valores_pares = 0
for numero in tupla:
    if numero % 2 == 0:
        valores_pares += 1
print(f'Foram digitados {valores_pares} valores pares')