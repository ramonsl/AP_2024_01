

cont=1
soma=0
n= int (input("Digite ate onde vc quer somar\n"))
while cont<=n:
    soma=soma+cont
    cont+=1
print(soma)



soma=0
n= int (input("Digite ate onde vc quer somar\n"))
for cont in range (1,n+1):
    soma=soma+cont
print(soma)