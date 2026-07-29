nome = str(input('Nome: '))
data = int(input('Data de Nascimento: '))
carteira = int(input('Carteira de Trabalho: (0 Não Tem)   '))

dicionario = {'nome':nome,'data':data,'carteira':carteira}

if carteira != 0:
    ano = int(input('Ano de Contratação: '))
    salario = int(input('Salario: '))
    dicionario['ano'] = ano
    dicionario['salario'] = salario

print('-=-='*15)

print(f'Nome: {dicionario["nome"]}')
print(f'Idade: {2026 - (dicionario["data"])}')
print(f'Ctps: {dicionario["carteira"]}')
if dicionario["carteira"] != 0:
    print(f'Contratação: {dicionario["ano"]}')
    print(f'Salario: {dicionario["salario"]}')
    print(f'Aposentadoria: {(dicionario["ano"]) + 65}')
