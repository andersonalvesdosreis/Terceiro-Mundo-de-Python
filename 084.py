contador = 0
lista_nomes = []
lista_peso = []
while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    lista_peso.append(peso)
    lista_nomes.append(nome)
    contador =+1
    pergunta = str(input('Quer continuar? (S/N)')).upper()
    if pergunta in 'S':
        continue
    else:
        break
maior_da_lista_peso = max(lista_peso)
menor_da_lista_peso = min(lista_peso)
