def fatorial(num,show=False):
    f = 1
    for n in range(num,0,-1):
        f *= n
        if show == True:
            if n == 1:
                print('1 = ', f)
            else:
                print(n,end=' x ')
        if show == False:
            print(f'{num}! = {f}')


print(fatorial(5,show =True))

