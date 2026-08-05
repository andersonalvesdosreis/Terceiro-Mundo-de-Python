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
    """
    Executa o fluxo principal do programa de análise financeira.

    FUNCIONAMENTO GERAL DO CÓDIGO:
    ------------------------------
    1. Validação de Entrada (analisar):
       - Solicita continuamente que o usuário digite um valor via teclado.
       - Chama a função 'analisar()' que tenta converter a entrada para 'float'.
       - Se for um texto inválido, exibe uma mensagem de erro em vermelho e repete o loop.

    2. Processamento e Tratamento:
       - Assim que um valor numérico válido é fornecido, ele é convertido para float 
         (substituindo vírgula por ponto, se necessário).

    3. Funções Auxiliares de Cálculo e Formatação:
       - mostrar(): Formata qualquer número para o padrão de moeda R$ (com 2 casas e vírgula).
       - met(): Calcula e formata a metade do número.
       - dobro(): Calcula e formata o dobro do número.
       - aumento(): Calcula e formata o número acrescido de 10%.
       - aumento2(): Calcula e formata o número acrescido de 20%.
       - novo_valor(): Formata o valor original para exibição.

    4. Saída de Dados (resumo):
       - Chama a função 'resumo()' que imprime na tela um painel organizado contendo 
         todos os resultados processados e encerra o programa (break).
    """
    while True:
        pergunta = input('Digite um valor: R$')
        if not analisar(pergunta):
            numero_novo = float(pergunta.replace(",", "."))
            resumo(numero_novo)
            pergunta2 = input('Deseja conhecer como a função funciona? (digite 1 para sim)')
            if pergunta2 == '1':
                help(funcao_principal)
                break
            else:
                break
        else:
            print(f'\033[31mERRO: ->{pergunta}, não se enquadra nos requisitos!\033[m')
            continue