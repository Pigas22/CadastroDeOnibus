"""
from interface.Tela_Deletar import Tela_Deletar
from interface.Tela_Consulta import Tela_Consulta
from interface.Tela_Alterar import Tela_Alterar

import PySimpleGUI as sg

matriz = [
    ['jsdbfj', 557, 'dm', 4174],
    ['asjfa', 456, 'abc', 4574],
    ['mjkg', 5343, 'vv', 7896],
    ['jbawr', 43, 'vix', 645]
]

janela = Tela_Alterar(matriz, 1)

while True:
    evento, valor = janela.read()

    if evento == sg.WIN_CLOSED:
        janela.close()
        break
"""
class Person():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e é do sexo {self.sexo}'
        

    def andar(self):
        print(f'{self.nome} está andando')


    def parar(self):
        print(f'{self.nome} está ', end='')
        if self.sexo.upper() == 'M':
            print('parado')
        else:
            print('parada')


class Student(Person):
    def __init__(self, nome, idade, sexo, matricula, curso):
        super().__init__(nome, idade, sexo)
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
        return f'{super().__str__()}\nMatrícula: {self.matricula}\nCurso: {self.curso}'

    def andar(self):
        super().andar()

    def parar(self):
        super().parar()
        

class Teacher(Person):
    def __init__(self, nome, idade, sexo, salario, HrTrabalhadas):
        super().__init__(nome, idade, sexo)
        self.salario = salario
        self.HrTrabalhadas = HrTrabalhadas

    def __str__(self):
        return f'{super().__str__()}\nSalário: {self.salario}\nHoras Trabalhadas: {self.HrTrabalhadas}'

    def andar(self):
        super().andar()

    def parar(self):
        super().parar()
        


if __name__ == '__main__':
    homens = mulheres = nao_binario = 0
    pessoas = []
    
    # pss1 = Person('João', 18, 'M')
    # pss2 = Student('Maria', 19, 'F', 456, 'SI')
    # pss3 = Teacher('Kleber', 35, 'M', 2500, 40)

    while True:
        print(10 * '-=' + ' Cadastro ' + 10 * '=-' )
        print("""
                 [1] - Pessoa
                 [2] - Estudante
                 [3] - Professor
            """)

        tipo = int(input('Qual o tipo do cadastro? '))
        print(30 * '-=')

        if tipo in [1, 2, 3]:
            nome = str(input('Nome: ')).strip().title()
            idade = int(input('Idade: '))
            sexo = str(input('Sexo [M/F/O]: ')).strip().upper()[0]

            if tipo == 1:
                pessoas.append(Person(nome, idade, sexo))

            elif tipo == 2:
                matricula = int(input('Matrícula: '))
                curso = str(input('Curso: ')).strip().upper()

                pessoas.append(Student(nome, idade, sexo, matricula, curso))

            elif tipo == 3:
                salario = float(input('Salário: '))
                HrTrabalhadas = int(input('Horas Trabalhadas: '))

                pessoas.append(Teacher(nome, idade, sexo, salario, HrTrabalhadas))

        else:
            print('Opção inválida!')
            continue

        
        escolha = str(input('Continuar? [S/N] ')).upper()[0]
        if escolha == 'N':
            print(30 * '-=')
            break

                 
    for user in pessoas:
        if user.sexo.upper() == 'M':
            homens += 1
            
        elif user.sexo.upper() == 'F':
            mulheres += 1

        else:
            nao_binario += 1

        print(f'{user.nome}: ', end='')
        if type(user) == Person:
            print('Pessoa')

        elif type(user) == Student:
            print('Estudante')

        elif type(user) == Teacher:
            print('Professor')

        # user.andar()
        # print(user)
        # user.parar()

        print(30 * '-=')
    
    print(f'Quantidade de homens e mulheres: {homens} H; {mulheres} M; {nao_binario} Não Binários')