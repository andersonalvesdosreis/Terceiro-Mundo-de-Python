import random
def soma_par(lst):
    print(f'Na lista {lst} temos:')
    contador = 0
    for num in lst:
        if num %2 == 0:
            contador += num
    print(f'{contador} como a soma dos numeros pares')

lista = [2,4,6,3,1,3,5,23,10]
print(soma_par(lista))
