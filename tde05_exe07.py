'''7.      Faça um algoritmo que lê dois
 valores e escreve cada um juntamente com a mensagem: 
 “É múltiplo de 2” ou “Não é múltiplo de dois”.
'''
 
numero=int(input("Digite o numero\n"))
if numero%2==0:
    print(f"o {numero} é multiplo 2")
else:
    print(f"o {numero} não é multiplo 2")
    
