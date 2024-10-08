numero_01=int(input("Digite o valor 1"))
numero_02=int(input("Digite o valor 2"))
operacao=int(input("1 para somar\n 2 para subtração\n 3 para dividir\n 4 para multiplicar") )
if operacao==1:
    print(f"soma igual:{numero_01+numero_02}")
elif operacao==2:
    print(f"subtraçao igual:{numero_01-numero_02}")
elif operacao==3:
    print(f"divisao igual:{numero_01/numero_02}")
elif operacao==4:
    print(f"multiplicacao igual:{numero_01*numero_02}")
else:
    print("Operaçao invalida")
