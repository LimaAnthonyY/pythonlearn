"""
            Function       |         Module              |           Package                     |       Library
   
    Item    
        Maça           ----                          ----                                    ---- 
            - Peso         |                             |                                       |
            - Valor        |  Sessão Frutas e verduras   |       Supermercado A                  |
            - Cor          |                             |                                       |
        Banana              >>>   Sessão beleza           >>>    Supermercado B                   >>>   Hypermarket
            - Peso         |                             |                                       |
            - Valor        |      Sessão carnes          |       Supermercado C                  |
            - Cor          |                             |                                       |
                       ----                          ----                                    ----
"""

# Functions 
    # DRY - Don't repeat yourself.
# Deixar 2 espaçoes apos a criação da função.
    # Parametro --> Argumento.
    # Default = Aquele que você define o valor no parametro.
    # Non-Default = Aquele que você nao define o valor no parametro.
    # Passar primeiro o argumento non-default primeiro.
    # Vários argumentos (xargs) indentificando o Parametro.
def boasVindas ():
    print('Ola Marcos!')
    print("Temos 5 laptops em estoque!")


boasVindas()

def somar():
    num1 = 10
    num2 = 5
    result = num1 + num2
    print(result)


somar()

# Parametros --> argumentos (Funções)
"""
def bvMarcos():
    print('Ola Marcos!')
    print("Temos 5 laptops em estoque!")


def bvRonaldo():
    print('Ola Ronaldo!')
    print("Temos 4 laptops em estoque!")


def bvLinda():
    print('Ola Linda!')
    print("Temos 2 laptops em estoque!")


bvMarcos()
bvRonaldo()
bvLinda()
"""

def bv(nome, quantidade):
    print(f"Olá {nome}.")
    print(f"Temos {str(quantidade)} laptops em estoque.")


bv('Marcos', 5)
bv('Ronaldo', 4)
bv('Linda', 2)

def bv2(nome, quantidade = 6): # def name(Non-Default, Default):
    print(f"Olá {nome}.")
    print(f"Temos {str(quantidade)} laptops em estoque.")


bv2('Marcos')

#Calcula e retorna um valor

def cliente1 (nome):
    print(f'Olá {nome}') # Só vai imprimir o argumento f'Olá {nome}'

cliente1('Maria')

def cliente2 (nome):
    return f'Olá {nome}' # Armazenou o argumento f'Olá {nome}'

print(cliente2('Jose'))

x = cliente1("Maria")
y = cliente2("Jose")

print(x)
print(y)

#Xargs with numbers

# Criar uma função que soma vários números

def soma(*numeros):     # Definimos uma varial que recebera X numeros
    total = 0           # Iniciamos uma variavel total para receber a soma desses números
    for num in numeros: # Criamos um loop de soma, que acaba quando o range dos numeros acabarem
        total += num    # calculo da soma total = total + num
    return total        # retorna o total da soma dos números


x = soma(2,3,4,7,4)     # Variavel que ira receber a função e definir os argumentos

print(x)                # Print


# Função que armazena numeros e strings (Dados)

# 2 ** significa que posso passar embaixo o parametro
def agencia(**carro):
    return carro

print(agencia(modelo = 'Gol', cor = 'Branca', motor = 1.0, placa = '1234'))
print(agencia(modelo = 'Gol', cor = 'Azul', motor = 1.0))
print(agencia(modelo = 'Gol', cor = 'Preto', motor = 1.0, placa = '1234'))

#print(agencia)

### Importando um modulo
# Qual é o numero fatorial de 4?
# 4! é => 4*3*2*1 = 24

import math # Para saber mais pesquisar nas livrarias do python sobre as funções que tem

print(math.factorial(4))

print(math.floor(2.7))  # static method always rounds down and returns the largest integer less than or equal to a given number.

print(math.ceil(2.7))   # static method always rounds up and returns the smallest integer greater than or equal to a given number.
