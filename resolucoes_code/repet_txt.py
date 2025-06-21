# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 

texto = input("Digite um texto: ")
numero = int(input("Digite a quantidade de vocês que seu texto deve ser repetido: "))

while numero > 0:
    print(texto)
    numero -= 1