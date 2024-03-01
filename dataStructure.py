## Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

cidade1 = 'Rio de Janeiro'
cidade2 = 'São paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
# Lista          0                1            2         3
# Lista         -4               -3           -2         -1

numeros = [2, 4, 6]
# Lista    0, 1, 2
# Lista   -3,-2,-1

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
