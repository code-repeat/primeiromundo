from random import choice
alu1 = input("Primeiro aluno: ")
alu2 = input("Segundo aluno: ")
alu3 = input("Terceiro aluno: ")
alu4 = input("Quarto aluno: ")
lista_alunos = [alu1, alu2, alu3, alu4]
print("O aluno que irá apagar o quadro será o {}".format(choice(lista_alunos)))