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
# Deixar 2 espaçoes apos a criação da função


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