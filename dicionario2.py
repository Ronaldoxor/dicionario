alunos = {} # dicionário vazio

for n in range(5): #inserir 5 itens
    ra = input('Informe o RA: ')
    nome = input('Informe o Nome: ')
    alunos[ra] = nome
print(alunos)

#Dicionário com outras estruturas
#Cada chave do dicionário pode conter apenas um valor
#Caso seja necessário armazenar mais valores, é necessário utilizar outra estrutura dentro do dicionário

#Dicionário com listas
#exemplo
#Chave RA dos alunos
#valor:lista de notas do aluno

notas = {'19011234' : [8.5,9,2.5,7,6],
         '10840284' : [8,9.5,10,7.5,5],
         '24091490' : [4,5,6,7,8]}

print(notas['19011234'])
print(notas['19011234'][0])