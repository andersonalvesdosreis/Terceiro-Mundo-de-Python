def met(num):
    metade = num/2
    return (f'R${metade:.2f}'.replace(".", ","))


def dobro(num):
    dobro = num*2
    return (f'R${dobro:.2f}'.replace(".", ","))


def aumento(num):
    novo_valor = num + ((num*10)/100)
    return (f'R${novo_valor:.2f}'.replace(".", ","))

def aumento2(num):
    novo_valor = num + ((num*20)/100)
    return (f'R${novo_valor:.2f}'.replace(".", ","))


def novo_valor(num):
    return (f'R${num:.2f}'.replace(".", ","))

def resumo(num):
    print('-='*15)
    print(' '*4,'Resumo do Valor',' '*4)
    print('-='*15)
    print(f'Preço a ser analisado: {novo_valor(num)}')
    print(f'Dobro do valor:        {dobro(num)}')
    print(f'Metade do valor:       {met(num)}')
    print(f'O valor +10%:          {aumento(num)}')
    print(f'O valor +20%:          {aumento2(num)}')
    print('-='*15)

def analisar(num):
    try:
        numero = float(num)
        return resumo(numero)
    except ValueError:
        print(f'\033[31mERRO: ->{num}, não se enquadra nos requisitos!\033m')