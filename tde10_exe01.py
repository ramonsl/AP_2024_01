'''Elabore um programa que calcule e escreva
a soma de 10 números lidos.Esse algorimo deve 
ser feito duas vezes uma 
usando o FOR e WHILE'''
cont=0 
'''para contar'''
soma=0 
''''para acumular'''
while cont<=2:
    numero1=int(input(f"Digite o numero {cont+1}\n"))
    soma=numero1+soma
    cont+=1
  
print(f"A soma atual é {soma}")


soma=0  
for i in range (2):
    numero1=int(input(f"Digite o numero {i+1}\n"))
    soma=numero1+soma
    print (soma)