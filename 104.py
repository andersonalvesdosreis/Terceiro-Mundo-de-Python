def leiaInt(caracter):
    if caracter.isnumeric():
        print(f'{caracter} é um numero!')
    else:
        print(f'{caracter} não é um numero!')


pergunta = input('Digite algo: ')
leiaInt(pergunta)
