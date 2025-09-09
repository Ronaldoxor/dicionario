pessoas = {}
for n in range(5):
    cpf = input('Informe o cpf: ')
    nome = input('Informe o nome: ')
    pessoas[cpf] = nome
print(pessoas)

produtos = {}
for n in range(5):
    nome = input('Informe o nome: ')
    preco = float(input('Informe o preço: '))
    produtos[nome] = preco

for chave,valor in produtos.items():
    if valor > 50:
        print(f'O produto {chave} tem preço superior a 50 reais')

alunos = {}

# Coleta as informações de cada aluno
for n in range(5):
    notas = []  # Lista de notas de cada aluno
    rm = input('rm: ')
    for n in range(3):
        nota1 = float(input(f'Informe a {n + 1} nota: '))
        notas.append(nota1)
    alunos[rm] = notas

# Calcula a média das notas de cada aluno
for rm, notas in alunos.items():  # Aqui usamos alunos.items() para pegar o rm e as notas do aluno
    soma = sum(notas)  # Soma as notas do aluno
    media = soma / len(notas)  # Calcula a média
    print(f'A média do aluno {rm} é: {media:.2f}')

vogais = { 'a' : 0,
           'e' : 0,
           'i' : 0,
           'o' : 0,
           'u' : 0}

texto = input('Digite um texto: ')
for x in texto:
    if x == 'a':
        vogais['a'] += 1
    elif x == 'e':
        vogais['e'] += 1
    elif x == 'i':
        vogais['i'] += 1
    elif x == 'o':
        vogais['o'] += 1
    elif x == 'u':
        vogais['u'] += 1

print(vogais)