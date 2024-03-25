
    # Python Object-Oriented Programmin

    # Classes
    #     Utilizadas para criar Objetos (instances)
    #     Objetos são partes dentro de uma Class (instancias)
    #     Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    #     ====
    #     Class: Frutas
    #     Objects: Abacate, banana...

from datetime import datetime

class Funcionarios:
    nome = 'Anthony'
    sobrenome = 'Lima'
    dataNascimento = '01/01/2000'

usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.dataNascimento)


    # Criar a classe
class Funcionarios:
    pass

    # Criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

    # Criar os parametros do usuário1
usuario1.nome = 'Anthony'
usuario1.sobrenome = 'Lima'
usuario1.dataNascimento = '01/01/2000'

    # Print
print(usuario1.nome)

    # Criar os parametros do usuário1
usuario2.nome = 'Limaa'
usuario2.sobrenome = 'Aanthony'
usuario2.dataNascimento = '02/01/2000'

print(usuario2.nome)

    # Diminuir os parametros
        # Criar a classe
class Funcionarios1:
        # Criar os argumentos para os parametros dentro de uma função
    def __init__(self, nome, sobrenome, dataNascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dataNascimento = dataNascimento                


        # Criar o objeto
usuario1 = Funcionarios1('Anthony', 'Lima', '01/01/2000')
usuario2 = Funcionarios1('Limaa', 'Aanthony', '02/01/2000')
usuario3 = Funcionarios1('Campelo', 'Eu', '03/01/2000')

        # Print
print(usuario1.nome)
print(usuario2.nome)
print(usuario3.nome)

    # Melhorando as classes
        # Diminuir os parametros
            # Criar a classe
class Funcionarios:
            # Criar os argumentos para os parametros dentro de uma função
    def __init__(self, nome, sobrenome, anoNascimento) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.anoNascimento = anoNascimento

    def nomeCompleto(self):
        return self.nome + ' ' + self.sobrenome
    
        # from datetime import datetime
    def idadeFuncionario(self):
        anoAtual = datetime.now().year
        self.anoNascimento = int(anoAtual - self.anoNascimento)
        return self.anoNascimento

            # Criar o objeto
usuario1 = Funcionarios('Anthony', 'Lima', 2000)
usuario2 = Funcionarios('Limaa', 'Aanthony', 2001)
usuario3 = Funcionarios('Campelo', 'Eu', 2002)


            # Print
#print(usuario1.nomeCompleto())
#print(usuario1.idadeFuncionario())
print(Funcionarios.nomeCompleto(usuario1))
print(Funcionarios.idadeFuncionario(usuario1))

