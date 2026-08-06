def LeiaFloat():
    while True:
        try:
            numero = float(input('Digite um numero Real: '))
        except (ValueError,TypeError):
            print(f'\033[31mERRO: não foi digitado um numero real valido!\033[m')
            continue
        else:
            return numero

def LeiaInt():
    while True:
        try:
            numero = int(input('Digite um numero inteiro: '))
        except (ValueError,TypeError):
            print(f'\033[31mERRO: não foi digitado um numero inteiro valido!\033[m')
            continue
        else:
            numero2 = LeiaFloat()
            print(f'Foi digitado de numero inteiro {numero} e de numero real {numero2}')
            break

LeiaInt()