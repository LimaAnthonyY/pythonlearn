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

