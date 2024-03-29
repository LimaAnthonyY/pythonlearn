# Aula 1
    # Comentario simples // simple comment
    # https://docs.python.org/3/library/functions.html (Built-in Functions)

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

# Aula 5

anoNas = input ("Digite em que ano você nasceu: ")
idade = 2024 - int(anoNas)

print ("Você tem " + str(idade) + " anos de idade")

# Aula 6

fruta = 'Abacaxi'
# index  0123456
print (fruta[3])
print (fruta[2:5]) #sempre o final será um numero anterior, exemplo se colocar 5 o ultimo sera o 4

valor = 99.75
# index 01234
valor = str(valor)

print (valor[3:5])

# Aula 7

'''
# O Marcos Silva é um excelente [Programador]
nome
sobrenome
profissão
texto
'''
nome = input ("Digite o seu nome: ")
sobrenome = input ("Digite o seu sobrenome: ")
profissao = input ("Digite a sua profissão: ")
texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' + '[' + profissao + ']'

texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}]'

print(texto)
print(texto2)

# Aula 8

msg = "Eu adoro comida caseira"
print(msg)

print(msg.lower()) #Tudo será impresso em caixa baixa
print(msg.upper()) #Tudo será impresso em caixa alta
print(msg.capitalize()) #Primeira letra será em caixa alta
print(msg.find('c')) #Vai me dizer em que posição esta a letra dentro do find, a letra tem que estar conforme o texto C ou c / -1 = não existe
print(msg.replace('a','e')) #Alterna a primeira letra ou palavra pela ultima ' '
print(msg.strip()) #Remove o espaço antes do primeiro caracter

# Aula 9

"""
== Equal
!= Not equal
> Greater than
< Less than
>= Greater than or equal to 
<= Less than or equal to
"""

op = 10 == 10
print(op)

op = 10 > 9
print(op)

op = 10 < 9
print(op)

op = 10 <= 9
print(op)

op = 10 >= 9
print(op)

# Aula 10

x = 10

x += 5 # x = x + 5 
print(x)

x -= 5 # x = x - 5 
print(x)

x *= 5 # x = x * 5 
print(x)

x /= 5 # x = x / 5 
print(x)

x %= 5 # x = x % 5 
print(x)

# Aula 11

vel = 100

if vel > 110:
    print("Você está acima da velocidade máxima permitida!")
    print("Reduza a sua velocidade até estar abaixo de 110KM/h!!")
elif vel < 60:
    print("Você está abaixo da velocidade máxima permitida!")
    print("Aumente a sua velocidade até o mínimo de 80KM/h!")
else :
    print("Você está dentro da velocidade permitida! :)")

# Aula 12

rendaAcima = True
nomeLimpo = True

if rendaAcima & nomeLimpo:
    print("Financiamento aprovado!")
else:
    print("Financiamento negado!")

if rendaAcima or nomeLimpo:
    print("Financiamento aprovado!")
else:
    print("Financiamento negado!")

# Aula 13

valor = 10

if valor >= 20 and valor < 40:
    print("Produto foi aceito!")
else:
    print("Produto não aceito!")


if 20 <= valor < 40:
    print("Produto foi aceito!")
else:
    print("Produto não aceito!")

## imprimir de 1 a 5 numeros

for i in range(5):
    print (i+1)

for numero in range(300):
    print(numero+1)

for letra in 'Google':
    print(letra)

palavra = "fantastico"

for letra in palavra:
    print(f"{letra} esta dentro da palavra {palavra}")

## Enviar um email com os detalhes da compra online (maximo 3 tentativas)
## para compras confirmadas.

compraConfirmada = False
dadosCompra = 'Compra no valor de 12.50 e entrega confirmada'

for enviar in range(3):
    if compraConfirmada:
        print(dadosCompra)
        print("Detalhes enviados para o seu e-mail")
        break
else:
    print("Compra não autorizada")

### Nested Loops
    
'''
for loop nested

       Outer loop
        inner loop
'''

for numero1 in range(5):
    print(numero1)
    for numero2 in range(5):
        print(numero2)


for numero1 in range(1,6):
    print('Produto ' + str(numero1))
    for numero2 in range(1,11):
        print(numero1, numero2)


## Separando STR
        
# Modificar a palavra fantastico para f a n t a s t i c o

for space in palavra:
    space = space.upper()
    print(f'{space} ', end='')


### Gerar um retangulo
    
"""
Criar um retangulo 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
"""
linhas = 6
colunas =  6
simbolos = '@'

for l in range(linhas) :
    for c in range(colunas):
        print(simbolos, end="")
    print("")

### while
"""
Loops dependentes de uma condição

#Criar uma promoção para um produto de 100R$
"""
price = 100.00
dia = 1 
while price > 20:
    print(f'No dia {dia} o produto vai ser vendido por R$ {price}')
    dia +=1
    price -=5

idade = 18
"""
Como seria:
if idade >= 16:
    votar = print("Voto permitido")
else:
    votar = print("Voto nao foi permitido")
Melhor forma para fazer:
"""
votar = 'Voto permitido' if idade >= 16 else 'Voto nao permitido'
print(votar)

## Diferença de for loop e while loop
    # if só roda uma vez verdadeiro ou falso
    # for roda até um certo numero X
    # while ira até satisfazer uma condição

## Publicar um produto com comissão de 10% se for acima de R$ 20

produto = float(input("Digite o valor do produto: "))
porcentagem = 10/100

while valor > 20:
    valor = produto * porcentagem + produto 
    print(f'O valor do produto será de {valor}')
    break

if float(produto) > 20:
    valor = produto * porcentagem + produto 
    print(f'O valor do produto será de {valor}')
else:
    print(f'O valor do produto será de {valor}')