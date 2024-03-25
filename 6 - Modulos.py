import funcoes # Importa tudo que está dentro de funcoes

from funcoes import somar # Só vou importa o somar dentro de funcoes

from funcoes import * # Pode ser feito assim, porém não é recomendavel devido a quantidade de funções que o codigo pode ter.

funcoes.mult() # Como não coloquei o from é preciso colocar o funcoes. anterior a função
somar() # Não preciso colocar o funcoes. como no anterior


    # Para packages é importante colocar uma função __init__.py para que o python reconheça como package
    # Apos isso from com o nome da pasta.nome_da_biblioteca e por fim nome da função
from Itens.calculo import func
from Itens.cadastro import cliente, cliente2  
cliente()
cliente2()
func()

list1 = ['a', 'b', 'c', 'd', 'e']
var1 = findIndex(list1, 'g')

if var1 != -1:
    print(f'Está localizado dentro do index na posição : {var1}')    
else:
    print("Não localizado")


