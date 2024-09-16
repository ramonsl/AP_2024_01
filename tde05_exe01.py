#1. Dados dois números A e B, some 100 ao maior número e imprima.

numero_A=int(input("Digite o número A:\n"))
numero_B=int(input("Digite o número B:\n"))
'''
if numero_A>numero_B:
    print(f"o maior numero é {numero_A} e a soma é: {numero_A+100}")
else:
    print(f"o maior numero é {numero_B} e a soma é: {numero_B+100}")


if numero_A > numero_B:
    maior=numero_A
else: 
    maior=numero_B
print (f"o maior numero é {maior} e sua soma é: {maior+100}")
'''

if numero_A<numero_B:
    print(f"o maior numero é {numero_B} e a soma é: {numero_B+100}")
else:
    print(f"o maior numero é {numero_A} e a soma é: {numero_A+100}")