par = []
impar = []
for n in range(1,8):
    pergunta = int(input(f'Digite o valor {n}: '))
    if pergunta %2 == 0:
        par.append(pergunta)
    else:
        impar.append(pergunta)
    par.sort()
    impar.sort()
print('#'*20)
print(f'Os valores par são {par}')
print(f'Os valores impares são {impar}')
print('#'*20)
