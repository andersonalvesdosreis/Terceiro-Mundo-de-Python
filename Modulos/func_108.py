def met(num):
    metade = num/2
    return (f'R${metade:.2f}'.replace(".", ","))


def dobro(num):
    dobro = num*2
    return (f'R${dobro:.2f}'.replace(".", ","))


def aumento(num):
    novo_valor = num + ((num*10)/100)
    return (f'R${novo_valor:.2f}'.replace(".", ","))


def novo_valor(num):
    return (f'{num:.2f}'.replace(".", ","))