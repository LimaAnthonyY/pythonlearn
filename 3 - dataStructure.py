## Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

cidade1 = 'Rio de Janeiro'
cidade2 = 'São paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
# Lista          0                1            2         3
# Lista         -4               -3           -2         -1
    # Colocar um espaço após a virgula.

numeros = [2, 4, 6]
# Lista    0, 1, 2
# Lista   -3,-2,-1
    # Colocar um espaço após a virgula.

## Trazer todos os Index dessa lista
print(cidades)
print(numeros)

## Trazer apenas um Index
print(cidades[2])
print(cidades[-1])
print(numeros[1])
print(numeros[-1])

## Atualizar um Index dentro dessa lista
print(cidades)  # Antes da atualização
cidades[0] = 'Brasilia' # Substituindo Rio de Janeiro por Brasilia
print(cidades)  # Após a atualização

## list functions python (https://docs.python.org/3/tutorial/datastructures.html)
    # Exemplos

cidades.append('Rio de janeiro') # Adicionando o Rio de janeiro de volta *Só que no final da lista
# nomedaLista.append('Novo Index') = adiciona ao final
print(cidades)

cidades.remove('Brasilia') # Remove o index que der match* Tem que estar escrito igual a lista
# nomedaLista.remove('Nome do Index') = Remove independete do Local
print(cidades)

cidades.insert(0, 'Brasilia') # Insere o Index na posição que foi especificado na sintax
# nomedaLista.insert(x, 'Nome do Index') = Inserir no local especificado
print(cidades)

cidades.pop(0) # Remove o index da posição especificada
# nomedaLista.pop(posição X) = Remove a index da posição especificada
print(cidades)

## Concatenação 

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

final = numeros * 2 # Repete a lista por * N numeros
print(final)

final = numeros + letras # Soma as duas listas fazendo assim uma concatenação
print(final)

numeros.extend(letras) # Faço uma extensão da lista x adicionando outra lista a ela
print(numeros)

itens = [['item1', 'item2'], ['item3', 'item4']]
# lista  [   0   ,   1   ], [    0   ,   1   ]  Interno = y
# lista [        0        ,          1         ]  Externo = x
#print(list[x][y]) Imprimi dentro do Index externo x o index interno y
print(itens) # Imprimi a lista inteira
print(itens[0]) # Imprimi apenas o Index externo x
print(itens[0][1]) # Imprimi dentro do Index externo n o index interno n
print(itens[1][0]) # Imprimi dentro do Index externo n o index interno n


##   Unpacking Lists / associação das variaveis.

produtos = ['arroz', 'feijão', 'laranja', 'banana']
# lista        0         1         2         3
"""
item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]

print(item1)
print(item2)
print(item3)
print(item4)
"""

# item1, item2, item3, item4 = produtos # faz o unpacking de todos os itens, o produto[0] = item1 e assim por diante
item1, item2, *outros = produtos # faz o unpacking e o *outros joga os que sobraram para outros (como um mini lixo)
    ## Para esse tipo de unpacking é necessario sempre direcionar todos os valores pra algum lugar, por isso utilizamos o *var para jogar os que sobraram para o "Lixo"
item1, item2, *outros, item4 = produtos    
    ## O "Lixo" pode ficar no meio também com isso ele vai pegar os itens que não foram especificados
print(item1)
print(item2)
# print(item3)
# print(item4)

## Looping dentro de lista

valores = [50, 80, 110, 150, 170]

for x in valores:
    print(f'O valor final do produto é de R$ {x:.2f}')


cores = ['amarelo', 'verde', 'azul', 'vermelho']

cliente = input(f'Qual a cor você deseja? ')
cliente = cliente.lower() # tratativa do que o cliente digitou para se adequar a lista em caixa baixa

if cliente in cores:
    print(f'A cor {cliente} está disponivel')
else:
    print(f'A cor {cliente} não está disponivel em estoque')

# var = list('comprar')
# print(var)

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

# zipar 2 listas
x = zip(cores, valores)

print(list(x))

    # Crar uma lista de frutas a partir do input fornecido pelo usuário

frutasUser = input('Por favor digitar as frutas da lista separado por virgula.\n(exemplo: banana,uva)\n')

frutasList = frutasUser.split(',')

print(frutasList)

    # Tuples
        # Armaenar mais de uma informação em variáveis
        # Manter a sequencia dos dados em uma variavel
        # Não podem ser alteradas (Immutable)
        # Não posso remover, alterar ou adiconar qualquer coisa nesse tipo
        # Tuple ocupa menos memoria, além de ser mais rapida. Sendo vantajosa em itens que não vao ser alterados.
coresList =  ['amarelo', 'verde', 'azul', 'vermelho']
coresTuple =  ('amarelo', 'verde', 'azul', 'vermelho')

print(coresList)
print(coresTuple)

dobleList = coresList * 2
dobleTuple = coresTuple * 2

print(dobleList)
print(dobleTuple)


    # Array(matriz)
        # Similar a listas
        # Melhor performance
        # Precisa importar com 'from array import array'
        # https://docs.python.org/3/library/array.html
from array import array

letras = ['a', 'b', 'c', 'd']
numI = [10, 20, 30, 40]
numF = [1.2, 2.2, 3.2, 4.2]

letras = array('u', ['a', 'b', 'c', 'd'])
numI = array('i',[10, 20, 30, 40])
numF = array('f',[1.2, 2.2, 3.2, 4.2])

print(letras)
print(numI)
print(numF)

    # Set (Listas)
        # Similar a listas
        # Evita itens duplicados
        # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union (vai juntar as duas listas retirando os repetidos)
print(num1 - num2) # Difference (Vai tirar do 1 os numeros que tem repetidos com o segundo)
print(num1 ^ num2) # Symmetric Difference (Vai mostrar os valores que não são repetidos)
print(num1 & num2) # And (Vai mostrar os números que tem nas 2 listas)

print(len(num1))

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2) # Union (vai juntar as duas listas retirando os repetidos)
set5 = set1.difference(set3) # Difference (Vai tirar do 1 os numeros que tem repetidos com o segundo)
set6 = set1.intersection(set2) # Intersection (O que tem no 1 e no 2)
set7 = set1.symmetric_difference(set3) # Symmetric Difference (Vai mostrar os valores que não são repetidos)

print(set4)
print(set5)
print(set6)
print(set7)

list1 = set([10, 20, 30, 40, 50])

s1 = {1, 2, 3, 4, 5, 6}
print(f'Apos a declaração do Set: {s1}')

s1.add(7) # Vai adicionar 1 unico numero ao ( N )
print(f'Apos a adição no Set do numero 7: {s1}')

s1.add(4) # não vai adicionar o 4, pois evita numeros duplicados
print(f'Apos a adição no Set do numero 4: {s1}')

s1.update({7, 8, 9, 10}) # Vai adicionar todos dentro do ({ N })
print(f'Apos a adição no Set dos numeros [7, 8, 9, 10]: {s1}')

s1.remove(10) # Vai remover o item dentro do ( N ) // Gera um erro se o número não existir
print(f'Apos a remoção do numero 10: {s1}')

s1.discard(9) # Vai discartar o número 9 // Não gera um erro se o número não existir
print(f'Apos discartar o numero 9: {s1}')


    # Dicíonários
        # Utiliza index no formato de Keys e Values
        # Aceita string, integer, float, boolean ... 

alunos = {'nome': 'Ana', 'idade': 16, 'nota final': 'A', 'aprovação': True} # nome = {keys: values, keys2: values2, n: n }

print(alunos['nome'])

alunos = {'nome': 'Ana', 'idade': 16, 'nota final': 'A', 'aprovação': True}

alunos['nome'] = 'Jose'
alunos.update({'nome': 'Carlos', 'nota final': 'B'})
print(alunos['nome']  + ' ' + alunos['nota final'])

alunos.update({'endereço': 'Rua A'})
print(alunos)

print(alunos.get('bairro', 'Não existe')) # utilizando o get, eu peço a key + value e colocar uma mensagem de retorno
    # Utilizar o get te traz uma mensagem de erro, e não para o programa.
    # print(alunos['bairro']) -- te traz uma mensagem de erro parando o programa

del alunos['idade'] # remover do dicionario
