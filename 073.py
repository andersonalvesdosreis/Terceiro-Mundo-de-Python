lista_b = ('Palmeiras','Flamengo','Fluminense','São paulo','Athletico-PR','Coritiba','Bahia','Athletico-MG','Internacional','Brangatino','Vasco da Gama','Cruzeiro','EC Vitória','Botafogo','Corinthians','Santos','Gremio','Mirassol','Remo','Chapecoense')
print('='*20,'Tabela do Brasileirão','='*20)
print(lista_b)
print('='*20,'Os primeiros 4','='*20)
print(lista_b[0:5])
print('='*20,'Os ultimos 4','='*20)
print(lista_b[-1],lista_b[-2],lista_b[-3],lista_b[-4])
print('='*20,'Os primeiros 2 em Ordem alfabetica','='*20)
lista_a = []
for letra_A in lista_b:
    if letra_A.count('A'or'a',0) == 1:
        lista_a.append(letra_A)
print(lista_a)