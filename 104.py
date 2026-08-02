def leiaInt(caracter):
    while True:
        pergunta_p = input(caracter)
        if pergunta_p.isnumeric():
            print(f'{pergunta_p} é um numero!')
            break
        else:
            print('\033[31mERRO DIGITE UM NUMERO INTEIRO!\033[m')
            continue


pergunta = leiaInt('Digite algo: ')