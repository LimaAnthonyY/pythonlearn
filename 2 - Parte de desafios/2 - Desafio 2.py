    # Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para
pintar uma parede. O usuário deverá fornecer as seguintes
informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x 
latas de tinta'
'''
from Func2 import tint

r = float(input("Digite o rendimento da tinta: "))
a = float(input("Digite a altura da parede: "))
l = float(input("Digite a largura da parede: "))

var = tint(r,a,l)

print(f"Você necessita de {var} latas de tinta.")