numero_01=int(input("Digite um numero 01\n"))
numero_02=int(input("Digite um numero 02\n"))
numero_03=int(input("Digite um numero 03\n"))

if numero_01>= numero_02 and numero_01>=numero_03:
    print(f"o maior numero é {numero_01}")
elif numero_02>= numero_01 and numero_02>=numero_03:
    print(f"o maior numero é {numero_02}")
else:
    print(f"o maior numero é {numero_03}")



if numero_01>= numero_02 and numero_01>=numero_03:
    maior=numero_01
elif numero_02>= numero_01 and numero_02>=numero_03:
    maior=numero_02
else:
    maior=numero_03
    
print(f"o maior numero é {maior}")


