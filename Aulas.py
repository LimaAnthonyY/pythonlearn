
# Comentario simples // simple comment
# Aula 1

print("hello word")
print('How are u?')
print("What day is it?")

# Aula 2
'''
Comentario de várias linhas // Multi-line comment

print("hello word")
print('How are u?')
print("What day is it?")
'''

# Aula 3
'''
Text => String/ str=("Texto")
Numbers => Integer/ int=(1,2,3...N)
Float => Quebrado/ float=(3,5 / 2,1 ...)
Boolean type => Bool: True or False
'''

x = str(3)
y = int(4)
z = float(5)

print(x + x)
print(y + y)
print(z + z)

# Aula 4



'''
o Andre tem 32 anos de idade e mora na cidade de São Paulo
Nome = variavel
Idade = variavel
Cidade = variavel
'''

nome = 'Andre'
idade = 32
cidade ='São Paulo'

print("O " + nome + " tem " + str(idade) + " anos de idade e mora em " + cidade + ".")

nome = "Anthony"
idade = 23

print("O " + nome + " tem " + str(idade) + " anos de idade e mora em " + cidade + ".")

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
cidade = input("Digite a sua cidade: ")

print("O/A " + nome + " tem " + str(idade) + " anos de idade e mora em " + cidade + ".")

#Aula 5

anoNas = input ("Digite em que ano você nasceu: ")
idade = 2024 - int(anoNas)

print ("Você tem " + str(idade) + " anos de idade")



#Aula 6

fruta = 'Abacaxi'
#index   0123456
print (fruta[3])
print (fruta[2:5]) #sempre o final será um numero anterior, exemplo se colocar 5 o ultimo sera o 4

valor = 99.75
#index  01234
valor = str(valor)

print (valor[3:5])
