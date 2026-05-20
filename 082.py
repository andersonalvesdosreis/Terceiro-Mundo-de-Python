lista = []
impar = []
par = []
while True:
    pergunta = int(input('Digite um numero: '))
    lista.append(pergunta)
    if pergunta %2 == 0:
        par.append(pergunta)
    else:
        impar.append(pergunta)
    pergunta2 = str(input('Deseja continuar? (s/n): ')).lower()
    if pergunta2 in 's':
        continue
    else:
        break
print(f'A lista foi: {lista}')
print(f'Lista dos pares {par}')
print(f'Lista dos impares {impar}')
