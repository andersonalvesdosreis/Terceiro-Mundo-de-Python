ano = 2026
def voto(ano_nasc):
    idade_minima = 2010
    idade_minima_maxima = 2009
    if ano_nasc == idade_minima:
        print(f'Com {ano - ano_nasc} anos: Voto Opcional')
    elif ano_nasc == idade_minima_maxima:
        print(f'Com {ano - ano_nasc} anos: Voto Opcional')
    elif ano_nasc > idade_minima:
        print(f'Com {ano - ano_nasc} anos: Não Vota!')
    else:
        print(f'Com {ano - ano_nasc} anos: Voto Obrigatorio!')


pergunta = int(input('Digite seu ano de nascimento: '))
voto(pergunta)

