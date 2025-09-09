#São delimitados por chaves { }
#Seus itens são separados vírgulas ,
#Cada item é composto por uma chave e um valor, separados por dois-pontos :

dicionario = {'name' : 'Bob',
              'age' : 25,
              'job' : 'Dev',
              'city' : 'New York',
              'email' : 'bob@web.com'}

#Características do dicionário
#Não possuem índices sequenciais
#São estruturas heterogênesa
#As chaves e os valores podem ser de quaisquer tipos
#São Mutáveis
#Os valores podem ser alterados
#as chaves não podem ser alteradas
#Chaves devem ser únicas
#Acessar itens
#Para acessar as informações do dicionário, devemos utilizar suas chaves.

dicionario2 = {'Banana' : 3.00,
               'Laranja' : 5.00,
               'Uva' : 8.00}

dicionario2['Uva'] = 10.00 #Alterar o valor associado à chave

print(dicionario2) #imprimir dicionário
print(dicionario2['Banana']) #imprimir valor

#Inserir item

#Para inserir um item ao dicionário, deve-se atriburi um valor a uma chave inexistente
#Se a chave não existir, ela será criada
#Dicionário não possui a função append

dicionario3 = {'Banana' : 3.00,
               'Laranja' : 5.00,
               'Uva' : 8.00}

dicionario3['Melancia'] = 12.00 #inserir novo item
dicionario3['Abacaxi'] = 10.00 #inserir novo item

print(dicionario3)

#Remover itens

#para remover um item do dicionário, pode-se utilizar a função pop
#Indicar a chave como parâmetro
#No caso da chave inexistente, ocorrerá um erro

dicionario4 = {'Banana' : 3.00,
               'Laranja' : 5.00,
               'Uva' : 8.00}

#Percorrer valreos do dicionário
#A estrutura for pode ser utilizada para percorrer os valores(values) e chaves(keys) do dicionário

for n in dicionario4.keys():
    print(n) #imprime todas as chaves

for n in dicionario4.values():
    print(n) #imprime todos os valores

for chave,valor in dicionario4.items():
    print(chave,valor) #imprime todos os itens

dicionario4.pop('Laranja') #Exclui item e chave

#Operador in

#O operador in pode ser utilizado para verificar se uma chave existe no dicionário

dicionario5 = {'Banana' : 3.00,
               'Laranja' : 5.00,
               'Uva' : 8.00}

if 'Abacaxi' in dicionario5:
    print('A chave existe no dicionário')
else:
    print('A chave não existe no dicionário')