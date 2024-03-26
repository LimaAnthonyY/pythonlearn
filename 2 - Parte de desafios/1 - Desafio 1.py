# Desafio com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em Celsius) do steak
ele retorna o ponto de cozimento em portugues. O usuário deverá fornecer
a temperatura

Temperaturas - Cozimento
120 F ou 48 C - Rare (Selada)
130 F ou 54 C - Medium Rare (Ao ponto para o mal)
140 F ou 60 C - Medium  (Ao ponto)
150 F ou 65 C - Medium Well (Ao ponto para o bem)
160 F ou 71 C - Well done (Bem passada)
'''
from Func import temp

try:
    idioma = int(input('*Qual idioma deseja continuar?\n  1- Portugues\n  2- Ingles\n\n1*What language do you want?\n  1- Portuguese\n  2- English\n======'))
    temp(idioma)
except ValueError:
        print("Digite um valor valido.")
        idioma = input('Deseja sair? 1- Não 2- Sim\n====== ')
        temp(2)