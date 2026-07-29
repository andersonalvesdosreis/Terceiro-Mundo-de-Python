contador = 0
contador2 = 0
lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    media = (nota1+nota2)/2
    lista_nova = [[nome],[nota1],[nota2],[media]]
    lista.append(lista_nova)
    contador2 += 0
    pergunta = str(input('Deseja continuar? [S/N]'))
    if pergunta == 'S' or pergunta == 's':
        continue
    else:
        break

print('-=-='*15)

for nome,nota1,nota2,media in lista:
    contador += 1
    print(f'O Aluno N*{contador - 1}, Esta Cadastrado com o Nome {nome}, Com a nota1 {nota1}, Com a nota2 {nota2}, E com Media {media}')

print('-=-='*15)

while True:
    x = int(input('Deseja consultar as notas de qual aluno? (DIGITE 999 Para Sair)'))
    if x != 999:
        print(f'O Aluno {lista[x][0]} Tirou {lista[x][1]} na primeira avaliação e {lista[x][2]} na segunda1')
        continue
    else:
        break

print('-=-='*15)
