    # Erros
        # Excelente para testes
        # Não realiza o 'stop code' no programa
        # Mensagems customizadas quando ocorre o erro
try:
    letras = ['a', 'b', 'c', 'd']
    print(letras[6])
except IndexError:
    print('Deu ruim')

try:
    valor = int(input('Digite o valor do produto: '))
    print(valor)
except ValueError:
    print('Digite um número valido!')
else:
    print('Usuario digitou um valor valido')
    resultado = valor * 2
    print(f'{str(resultado)}\n')


try:
    valor = int(input('Digite o valor do produto: '))
    print(valor)
except ValueError:
    print('Digite um número valido!')
finally:
    print('Ok')

print('Chegou sem parar o código!')