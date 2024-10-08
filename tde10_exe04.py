'''Efetue um programa que leia a
nota de 10 alunos de uma turma. 
Ao final, deve ser escrita a média geral 
da turma. 
Esse algoritmo deve ser feito
duas vezes, uma usando o FOR, e WHILE'''
cont=0
nota_total=0
while cont<10:
    nota=float(input(f"Digite a nota do aluno:{cont+1} "))
    nota_total=nota_total+nota
    cont=cont+1

media=nota_total/10
print(f"a média é {media}")

nota_total=0
for i in range (10):
    nota=float(input(f"Digite a nota do aluno:{i+1} "))
    nota_total=nota_total+nota
media=nota_total/10
print(f"a média é {media}")