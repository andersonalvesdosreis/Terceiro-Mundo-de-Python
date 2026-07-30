lista = []
lista_mulheres = []
contador = 0 
idade_de_todos = 0

while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    idade_de_todos += idade
    sexo = str(input('Sexo(M/F): ')) 
    if sexo != 'M' and sexo != 'F':
        print(f'Você digitou {sexo} que não se enquadra nas restrições tente novamente!') 
        print('Digite novamente!')
        sexo = str(input('Sexo(M/F): '))
    if sexo in 'Ff':
        lista_mulheres.append(nome)
    discionario = {'nome':nome,'idade':idade,'sexo':sexo}
    lista.append(discionario)
    contador += 1
    pergunta = str(input('Quer Continuar?(S/N) '))
    if pergunta in 'Ss':
        continue
    elif pergunta in 'Nn':
        break
    else:
        print(f'Você digitou {pergunta} que não se enquadra nas restrições tente novamente!') 
        pergunta = str(input('Quer Continuar?(S/N) '))

print('-=-='*15)

print(f'Tivemos ao todo {contador} Cadastros!')

media = (idade_de_todos) / (contador)

print(f'A Média das Idades foram de {media}')
print(f'As Mulheres cadastradas foram: {lista_mulheres}')

print('As pessoas Cadastradas Acima da Média foram:')
if idade > media:
    print(f'nome: {nome},idade: {idade},sexo: {sexo}')
