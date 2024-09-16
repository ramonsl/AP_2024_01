#2.Faça um algoritmo para determinar se 
# uma pessoa é maior ou menor de idade.

idade=int(input("Digite a idade"))
''''
if idade>=18 :
    print(f"você é maior de idade sua idade é {idade}")
else:
    print(f"você é menor de idade sua idade é {idade}")
    
if idade<=18 :
    print(f"você é menor de idade sua idade é {idade}")
else:
    print(f"você é maior de idade sua idade é {idade}")
'''

#nao fazer dessa forma, salvo for prova e vc 
# nao saber fazer de outra
if idade>=18:
    print(f"você é maior de idade sua idade é {idade}")
if idade <18:
    print(f"você é menor de idade sua idade é {idade}")
