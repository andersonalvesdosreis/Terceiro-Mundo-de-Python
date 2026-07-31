
def analisador(*num):
    lista = [*num]
    qnt = len(lista)
    valor_maximo = max(lista)
    print('-='*20)
    print(f'A lista informada é {lista}')
    print(f'Foram informados {qnt} numeros na lista')
    print(f'O Valor maior da lista é: {valor_maximo}')
    print('-='*20)

#Teste
analisador(2,9,4,5,7,1)
analisador(4,7,0)
analisador(8,900000,3)
