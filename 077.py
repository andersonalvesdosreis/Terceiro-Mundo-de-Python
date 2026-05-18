vogais = ('a','e','i','o','u')
pergunta = str(input('Digite uma palavra: ')).lower()
num_vogais = 0
vogaisl = []
for letra in pergunta:
    if letra in vogais:
        num_vogais += 1
        vogaisl.append(letra)
print(f'A {num_vogais} vogais nessa palavra e são: {vogaisl}')