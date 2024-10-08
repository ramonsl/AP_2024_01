'''Efetue um programa que mostre
todos os números inteiros ímpares 
situados na faixa de 1000 a 1500. 
Esse algoritmo deve ser feito 
duas vezes, uma usando o FOR,WHILE;'''

cont =1000
while cont<1500:
    if cont %2 != 0:
        print (cont)
    cont+=1

for i in range (1000, 1500):
    if i %2 != 0:
        print(i)
  


