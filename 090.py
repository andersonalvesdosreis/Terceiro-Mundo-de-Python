nome = str(input('Nome: '))
media = int(input(f'Media de {nome}: '))
print(' '*20)
aluno = {'nome':nome,'media':media}
print(f'Nome: {aluno["nome"]}, Media: {aluno["media"]}')
