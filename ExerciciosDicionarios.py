#Exercício 1

#Preencha um dicionário com as informações de 5 pessoas.
#Utilize o cpf da passoa como chave e o nome como valor.
#Solicite os dados ao usuário.

pessoas = {}
for n in range(5):
    cpf = input('Informe o cpf: ')
    nome = input('Informe o nome: ')
    pessoas[cpf] = nome
print(pessoas)

#Exercicio 2

#Preencha um dicionário com as informações de 5 produtos.
#Utilize o nome do produto como chave e o preço como valor.
#Solicite os dados ao usuário.
#Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00

produtos = {}
for n in range(5):
    nome = input('Informe o nome: ')
    preco = float(input('Informe o preço: '))
    produtos[nome] = preco

for chave,valor in produtos.items():
    if valor > 50:
        print(f'O produto {chave} tem preço superior a 50 reais')

#Exercício 03

#Preencha um dicionário com os dados de 5 alunos.
#Utilize o RM do aluno como chave e uma lista de três notas como valor.
#Solicite os dados ao usuário.
#Percorra o dicionário e exiba a média de cada aluno.

alunos = {}

# Coleta as informações de cada aluno
for n in range(5):
    notas = []  # Lista de notas de cada aluno
    rm = input('Digite seu rm: ')
    for n in range(3):
        nota1 = float(input(f'Informe a {n + 1} nota: '))
        notas.append(nota1)
    alunos[rm] = notas

# Calcula a média das notas de cada aluno
for rm, notas in alunos.items():  # Aqui usamos alunos.items() para pegar o rm e as notas do aluno
    soma = sum(notas)  # Soma as notas do aluno
    media = soma / len(notas)  # Calcula a média
    print(f'A média do aluno {rm} é: {media:.2f}')

#Exercício 04
#Conte a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é
#a vogal e o valor é a quantidade de vezes que essa vogal aparece no texto.

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

print("Foram encontradas as seguintes quantidades de cada vogal no texto: ")
print(vogais)