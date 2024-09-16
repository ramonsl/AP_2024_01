'''6.      Faça um algoritmo para ler dois valores:
NUM1 e NUM2, e se NUM1 for 
maior que NUM2 executa a soma de NUM1 e NUM2; 
caso contrário, executa uma subtração.'''

numero_01=int(input("Digite um numero 01\n"))
numero_02=int(input("Digite um numero 02\n"))

if numero_01>numero_02:
    print (f"a soma dos dois numeros é {numero_01+numero_02}")
elif numero_01==numero_02:
    print("Numeros iguais")
else:
    print (f"a diferença dos dois numeros é {numero_01-numero_02}")
