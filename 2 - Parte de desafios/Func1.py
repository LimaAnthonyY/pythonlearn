def temp(idioma):
    while(idioma!=3):
        try:
            if idioma == 1:
                user = int(input('Digite a temperatura da carne: '))

                if user < 48:
                    print(f"A carne ainda não está na temperatura mínima!")
                elif 48 <= user < 54:
                    print(f"48 C - Selada")
                elif 54 <= user < 60:
                    print(f"54 C - Ao ponto para o mal")
                elif 60 <= user < 65:
                    print(f"60 C - Ao ponto")
                elif 65 <= user < 71:
                    print(f"65 C - Ao ponto para o bem")
                elif 71 <= user <= 100:
                    print(f"71 C - Bem passada")
                else:
                    print(f"A carne queimou!")
                
                idioma = int(input('Deseja retornar ao menu de temperatura? 1- Sim 2- Não\n====== '))
                if idioma == 2:
                    break
                else:
                    temp(1)
            else:
                user = int(input('Enter the temperature of the steak: '))
                
                if user < 48:
                    print(f"The steak isn't at the minimum temperature yet!")
                elif 48 >= user < 54:
                    print(f"120 F - Rare")
                elif 54 >= user < 60:
                    print(f"130 F - Medium Rar")
                elif 60 >= user < 65:
                    print(f"140 F - Medium")
                elif 65 >= user < 71:
                    print(f"150 F - Medium Wel")
                elif 71 >= user <= 100:
                    print(f"160 F - Well done")
                else:
                    print(f"The steak is burnt!")
                
                idioma = int(input('Do you want to return to the temperature menu? 1- Yes 2- No\n====== '))
                if idioma == 2:
                    break
                else:
                    temp(1)
        except ValueError:
            print("Valor digitado fora do esperado. Digite um valor valido.")
            print('Deseja sair? 1- Não  2- Sim\n')
            print("Value entered not as expected. Enter a valid value.")
            idioma = input("Do you want to leave? 1- No 2- Yes\n====== ")
            if idioma == 2:
                break
            else:
                temp(1)