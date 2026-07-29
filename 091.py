import random

def quicksort_decrescente(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[-1]
    
    maiores = [x for x in lista[:-1] if x >= pivo]
    menores = [x for x in lista[:-1] if x < pivo]
    
    return quicksort_decrescente(maiores) + [pivo] + quicksort_decrescente(menores)


discionario = {
               'jogador1' : random.randint(1,6),
               'jogador2' : random.randint(1,6),
               'jogador3' : random.randint(1,6),
               'jogador4' : random.randint(1,6)
               }

print(' '*20)
print(f'O jogador1 tirou {discionario["jogador1"]}')
print(f'O jogador2 tirou {discionario["jogador2"]}')
print(f'O jogador3 tirou {discionario["jogador3"]}')
print(f'O jogador4 tirou {discionario["jogador4"]}')
print(' '*20)

print('Rankin:')

lista = [discionario["jogador1"],discionario["jogador2"],discionario["jogador3"],discionario["jogador4"]]

lista_ordenada = quicksort_decrescente(lista)

print("Pontuações do 1º ao 4º lugar:", lista_ordenada)
