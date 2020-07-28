import random
alu1 = input("Primeiro aluno: ")
alu2 = input("Segundo aluno: ")
alu3 = input("Terceiro aluno: ")
alu4 = input("Quarto aluno: ")

lista_alunos = [alu1, alu2, alu3, alu4]

print('ORDEM DE APRENSENTAÇÃO DO TRABALHO DE BIOLOGIA:')
print(f"{' '.join(random.sample(lista_alunos, 4))}")

#  outra forma seria utilizar o shuffle