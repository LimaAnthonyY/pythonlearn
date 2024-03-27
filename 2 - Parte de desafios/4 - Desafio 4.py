    # Calculo de IMC - Índice de Massa Corporal

'''
Qual é a sua altura em CM:
Qual é o seu peso em KG:
'''

from Func4 import imc

# Menor que 18,5      MAGREZA
# Entre 18,5 e 24,9   NORMAL
# Entre 25,0 e 29,9   SOBREPESO
# Entre 30,0 E 39,9   OBESIDADE
# Maior que 40,0      OBESIDADE GRAVE

al = float(input("Qual é a sua altura em cm: ")) 
pe = float(input("Qual é o seu peso em kg: ")) 

IMC = imc(al,pe)

try:
    if IMC <= 18.5:
        print("MAGREZA")
    elif 18.5 < IMC <= 24.9:
        print("NORMAL")
    elif 24.9 < IMC <= 29.9:
        print("SOBREPESO")
    elif 29.9 < IMC <= 39.9:
        print("OBESIDADE")
    else :
        print("OBESIDADE GRAVE")
except ValueError:
    print("Valor digitado invalido.\n\nFechando o programa\n------------------------------")