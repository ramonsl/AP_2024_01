'''Peça para os alunos acessarem e 
imprimirem as primeiras três
letras e as últimas três letras de uma string
fornecida.
'''
frase="Batatinha quando nasce"
fim=len(frase)-3;

print(frase[:3])
print(frase[fim:])

'''Usando fatiamento, 
inverta a palavra "Python" ("nohtyP").
'''


palavra="Python"
i=len(palavra)-1
novaPalavra=""
while i>=0:
    novaPalavra=novaPalavra+palavra[i]
    i=i-1
    
print(novaPalavra)

'''Use replace para substituir todas as ocorrências de
"e" por "E" em uma string fornecida.
'''
palavra= "Essa é a frase fornececida"
nova_palavra=palavra.replace("e", "E")
print(nova_palavra)
'''Transforme a frase "eu estou aprendendo python" 
para maiúsculas e depois divida a frase em palavras usando split.
'''
palavra= "eu estou aprendendo python"
palavra=palavra.upper()
print(palavra)
palavras=palavra.split()
print(palavras)

'''''Peça para os alunos verificarem se uma
frase fornecida começa com "Olá" e termina com "mundo".
'''

frase= input("Digite a frase")
if(frase.startswith("Olá")):
    print("Começa com Olá")
else:
    print("Não começa com Olá")
    
if (frase.endswith("mundo")):
    print("Termina com mundo")
else:
    print("Não termina com mundo")

'''Usar isalpha() para verificar se uma palavra
contém apenas letras e isdigit() para confirmar 
se uma string é um número.
'''
if frase.isdigit():
    print ('Frase são digitos')
else:
    print("Frase não é digito")
    
if frase.isalpha():
    print ('Frase são caracteres')
else:
    print("Frase nao são caracteres")