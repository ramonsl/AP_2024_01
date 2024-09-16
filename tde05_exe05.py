''' Faça um algoritmo para ler 
dois números. Se os números forem iguais, 
imprimir a mensagem: "NÚMEROS IGUAIS" e encerrar 
execução; caso contrário, imprimir o de maior valor.'''

numero_01=int(input("Digite um numero 01\n"))
numero_02=int(input("Digite um numero 02\n"))

if numero_01== numero_02:
    print ("Numeros Iguais.")
elif numero_01>numero_02:
    print (f"O numero maior é {numero_01}")
else:
    print (f"O numero maior é {numero_02}")

print("Usando a funcao max")
print (max(numero_01, numero_02))
