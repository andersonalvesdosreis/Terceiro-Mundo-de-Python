def ficha(nome='<desconhecido>',golos=0):
    global nome_jogador
    global g
    if nome_jogador.isalpha() == False:
        nome = '<desconhecido>'
    if g.isdigit() == False:
        golos = 0
    print(f'O jogador {nome} fez {golos} golos no campeonato')

nome_jogador = str(input('Nome jogador: ')).strip().capitalize()
g = input('Golos: ')
ficha(nome_jogador,g)