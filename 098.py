from time import sleep
def mostrar():
    print('-=-'*20)

def contagem(num1,num2,num3):
    if num3 == 0:
        num3 = 1
    if num3 < 0:
        num3 *= -1
    print(f'Contagem de {num1} a {num2} de {num3} em {num3}!')
    if num2 > num1:
       for x in range(num1,num2+1,num3):
          print(x,end=' ')
          sleep(0.5)
       print('Fim!')
    elif num1 > num2:
        for x in range(num1,num2+1,-num3):
            print(x,end=' ')
            sleep(0.5)
        print('Fim!')


contagem(1,10,1)

contagem(10,0,2)


print('Sua vez!')
pergunta = int(input('Inicio: '))
pergunta2 = int(input('Fim: '))
pergunta3 = int(input('Passo: '))
contagem(pergunta,pergunta2,pergunta3)
