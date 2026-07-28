num = [[],[]]
for n in range(1,8):
    pergunta = int(input(f'Digite o valor {n}: '))
    if pergunta %2 == 0:
        num[0].append(pergunta)
    else:
        num[1].append(pergunta)
    num[0].sort()
    num[1].sort()
print('#'*20)
print(f'Os valores par são {num[0]}')
print(f'Os valores impares são {num[1]}')
print('#'*20)
