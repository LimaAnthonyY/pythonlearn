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
from Func1 import temp

try:
    idioma = int(input('*Qual idioma deseja continuar?\n  1- Portugues\n  2- Ingles\n\n1*What language do you want?\n  1- Portuguese\n  2- English\n======'))
    temp(idioma)
except ValueError:
        print("Valor digitado fora do esperado. Digite um valor valido.")
        print('Deseja sair? 1- Não 2- Sim\n====== ')
        print("Value entered not as expected. Enter a valid value.")
        idioma = input("Do you want to leave? 1- No 2- Yes\n====== ")
        if idioma == 2:
            temp(3)
        else:
            try:
                idioma = int(input('*Qual idioma deseja continuar?\n  1- Portugues\n  2- Ingles\n\n1*What language do you want?\n  1- Portuguese\n  2- English\n======'))
                temp(idioma)
            except ValueError:
                    print("Valor digitado fora do esperado. Fechando o programa.\nEntered value not as expected. Closing the program.")
