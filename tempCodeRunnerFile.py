produto = input("Digite o valor do produto: ")
porcentagem = 10/100

if produto > 20:
    produto += (porcentagem * produto)
    print(f'O valor do produto é de {produto}')