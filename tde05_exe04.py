'''
 4.      Faça um algoritmo que 
 leia um número e mostre uma mensagem 
 indicando se este número é par ou ímpar 
 e se é positivo ou negativo.'''
 

numero=int(input("Digite um numero"))
 
if numero%2==0:
    print (f"Numero Par")
elif numero==0:
    print("numero zero")
else:
    print ("Numero impar")   
if numero >0:
    print ("Numero Posivo")
elif numero==0:
    print("numero zero")
else:
    print ("Numero negativo")

