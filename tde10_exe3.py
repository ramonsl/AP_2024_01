'''Efetue um programa que mostre todos os números inteiros ímpares situados numa  faixa de dois números digitados pelo usuário. Esse algoritmo deve ser feito duas vezes uma usando o WHILE e FOR;'''
cont =int(input("Digite o inicio"))
fim =int(input("Digite o fim"))

while cont<fim:
    if cont %2 != 0:
        print (cont)
    cont+=1

for i in range (cont, fim):
    if i %2 != 0:
        print(i)
  