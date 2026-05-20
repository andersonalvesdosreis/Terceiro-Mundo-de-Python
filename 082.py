lista = []
while True:
    pergunta = int(input('Digite um numero: '))
    lista.append(pergunta)
    pergunta2 = str(input('Deseja continuar? (s/n): ')).lower()
    if pergunta2 in 's':
        continue
    else:
        break
print(f'A lista foi: {lista}')