lista = []
contador = 0
while True:
    contador += 1
    lista.append(int(input('Digite um numero: ')))
    pergunta2 = str(input('Deseja continuar? (s/n): ')).lower()
    if pergunta2 in 's':
        continue
    else:
        break
print(f'Você digitou {contador} numeros!')
if 5 in lista:
    print('A o numero 5 na lista!')
lista.sort(reverse=True)
print(f'A lista em ordem decresente: {lista}')

