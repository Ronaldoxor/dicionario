#Set:
#Sets(conjuntos) são usados para armazenar uma coleção de dados
#um set é definido entre chaves {}.
#Um set é uma coleção não ordenada e não indexada

conjunto = {"apple","banana","cherry"}
print(conjunto)

conjunto2 = {"abc",34,40,"nome",1,1,True}
print(conjunto2)
#Retira as repetições e ordena os valores de forma crescente

#a função len() é utilizada para obter o tamanho de um conjunto
print(len(conjunto))

#Acessando itens
#Não é possível acessar itens consultando um índice ou uma chave
#Mas você pode percorrer os itens usando um for ou verificar se um valor está presente em um conjunto usando a instrução in

for x in conjunto:
    print(x)
    
#Inserindo itens:
#add

#Removendo itens
#remove
#Discard
#Remove gera erro, discard não gera erro

#Para criar um conjunto vazio, utilize a função set
#O metodo union cria um novo conjunto contendo todos os itens dos dois conjuntos

#O metodo intersection() retorna um conjunto que contém os itens que existem em ambos os conjuntos

x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}

z = x.intersection(y)

print(z)