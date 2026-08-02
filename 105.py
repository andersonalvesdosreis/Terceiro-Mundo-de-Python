def notas(*num,sit = False):
    """
    Função para Analisar notas!
    :Para n: Analisa notas uma ou mais(variavel o numero)
    :Para sit: Valor opcional, indicado se deve ou nao mostrar a situacao do aluno
    :return: Retorna a media em forma de discionario!
    """
    total = len(list(num))
    total_notas = sum(list(num))
    maximo = max(list(num))
    minimo = min(list(num))
    media = total_notas / total
    discionario = {'total':total,'maximo':maximo,'minimo':minimo,'media':media}
    if sit == True:
        situação = ''
        if media >= 6:
            situação = 'Média Boa'
        elif media >8:
            situação = 'Média Muito Boa!'
        else:
            situação = 'Média Baixa!'
        discionario['situação'] = situação
    print(discionario)

#Teste:
aluno_1 = notas(10,7,8,2,4)

aluno_2 = notas(1,10,9,8,sit=True)
