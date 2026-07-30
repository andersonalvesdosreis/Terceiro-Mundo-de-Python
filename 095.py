lista = []
n = 0
while True:
    nome = str(input('Nome do Jogador: '))
    num = int(input('O jogador jogou quantas partidas? '))
    contador = 0
    lista_de_gols = []
    for pergunta in range(1,num+1):
        pergunta1 = int(input(f'Quantos gols na {pergunta} partida? '))
        contador += pergunta1
        lista_de_gols.append(pergunta1)
    dict = {'nome':nome,'numeros':num,'lista':lista_de_gols,'total':contador}
    lista.append(dict)
    n += 1
    pergunta2 = str(input('Deseja Continuar? (S/N)'))
    if pergunta2 in 'Ss':
        continue
    else:
        break

print('-=-='*15)
print('No.___Nome____Num.Gols____TOTAL de Gols')
for jogador in range(0,n):
    print(f'{jogador}: {lista[jogador]["nome"]} {lista[jogador]["lista"]} {lista[jogador]["total"]}')

print('-=-='*15)

while True:
    x = int(input('Deseja consultar qual jogador? (DIGITE 999 Para Sair)'))
    if x != 999 and x <= n:
        print(f'O Jogador {lista[x]["nome"]} Jogou {lista[x]["numeros"]} partidas e realizou {lista[x]["total"]} gols no total')
        continue
    elif x != 999 and x > n:
        print('ERRO TENTE NOVAMENTE')
        continue
    else:
        break

print('-=-='*15)

while True:
    x = int(input('Deseja consultar tabela de qual jogador? (DIGITE 999 Para Sair)'))
    if x != 999 and x <= n:
        print(f'O Jogador {lista[x]["nome"]}')
        for posicao,numero in enumerate(lista[x]["lista"]):
            print(f'No {(posicao)+1} jogo ele realizou {numero} gols')
        continue
    elif x != 999 and x > n:
        print('ERRO TENTE NOVAMENTE')
        continue
    else:
        break

print('-=-='*15)