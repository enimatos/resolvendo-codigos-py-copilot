#Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 

numero = int(input("Digite um número inteiro: "))

if numero == 0:
    print(f"O número '0' é um número nulo'.")  
elif numero % 2 == 0:
    print(f"O número {numero} é par.") 
else:
    print(f"O número {numero} é ímpar.")
    