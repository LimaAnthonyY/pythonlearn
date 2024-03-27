    # Desafio com 'Set'
"""
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

lista1 = Funcionários que tem carro e trabalham a noite
lista2 = Funcionários que tem carro e trabalham durante o dia
lista3 = Funcionários que não tem carro
"""
from Func3 import lis

lista1 = set(lis.temCarro).intersection(lis.turnoNoite)
print(lista1)

lista2 = set(lis.temCarro).intersection(lis.turnoDia)
print(lista2)

lista3 = set(lis.funcionarios).difference(lis.temCarro)
print(lista3)