def mostrar(funcao):
    return (f'R${funcao:.2f}'.replace(".", ","))

def met(num):
    metade = num/2
    return mostrar(metade)


def dobro(num):
    dobro = num*2
    return mostrar(dobro)


def aumento(num):
    novo_valor = num + ((num*10)/100)
    return mostrar(novo_valor)

def aumento2(num):
    novo_valor = num + ((num*20)/100)
    return mostrar(novo_valor)


def novo_valor(num):
    return mostrar(num)

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
        numero = float(num.replace(",", "."))
        return False
    except ValueError:
        return True


def funcao_principal():
    while True:
        pergunta = input('Digite um valor: R$')
        if not analisar(pergunta):
            numero_novo = float(pergunta.replace(",", "."))
            resumo(numero_novo)
            break
        else:
            print(f'\033[31mERRO: ->{pergunta}, não se enquadra nos requisitos!\033[m')
            continue