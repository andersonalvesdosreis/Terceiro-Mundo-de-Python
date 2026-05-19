lista = []
for add in range(0,4):
    pergunta = int(input('Digite um numero: '))
    lista.append(pergunta)
print(lista)
print(f'O maior valor foi: {max(lista)}')
print(f'O menor valor foi: {min(lista)}')
