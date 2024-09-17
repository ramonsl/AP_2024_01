 '''9.      Faça um algoritmo que leia o
 número da conta bancária e o saldo de 
 um cliente. Caso a conta tenha saldo negativo, o programa deve enviar a 
 seguinte mensagem: CONTA ESTOURADA, caso contrário CONTA NORMAL.
 '''
 saldo=float(input("Digite o saldo"));
 conta= input( "Digite o numero da conta")
 
 if (saldo>0):
    print ("Conta Normal")
else:
    print("Conta estourada")
 