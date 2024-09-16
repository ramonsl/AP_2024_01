#3. Faça um algoritmo para 
# ler dois valores numéricos e 
# apresentar a diferença do maior pelo menor.
numero_a=int(input("Digite valor a\n"))
numero_b=int(input("Digite valor b\n"))

if numero_a==numero_b:
    print( f"Numeros iguais")
elif numero_a>numero_b:
    diferenca=numero_a - numero_b
    print( f"A diferença é {diferenca}")
else:
    diferenca=numero_b - numero_a
    print( f"A diferença é {diferenca}")

