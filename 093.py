nome = str(input('Nome do Jogador: '))
num = int(input('O jogador jogou quantas partidas? '))
contador = 0
for pergunta in range(1,num+1):
    pergunta1 = int(input(f'Quantos gols na {pergunta} partida? '))
    contador += pergunta1

dict = {'nome':nome,'numeros':num,'total':contador}

print('-=-='*15)

print(f'O Jogador {dict["nome"]} que jogou {dict["numeros"]} fez um total de {dict["total"]}gols.')

print('-=-='*15)
