num = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
while True:
    pergunta = int(input('Digite um numero entre 0 a 20: '))
    if pergunta in num:
        print(f'O numero {pergunta} esta entre 0 e 20!')
        break
    else:
        print('Seu numero não esta entre 0 a 20!')
        continue