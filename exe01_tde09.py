'''Solicitar a leitura de 10 valores inteiros,
ao final da leitura mostrar a soma dos números lidos, 
a média dos valores lidos.'''
cont=1
total=0
while cont<=10:
    num1=int(input(f"Digite o valor de {cont}\n"))
    cont=cont+1
    total=total+num1

print(f"total:{total}")
print(f"contagem {cont} média:{total/10}")
