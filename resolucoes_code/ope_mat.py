# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def soma(a, b): 
    return a + b
def subtracao(a, b): 
    return a - b
def multiplicacao(a, b): 
    return a * b
def divisão(a, b): 
    return a / b


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite a operação desejada (1- soma, 2 - subtracao, 3 - multiplicacao, 4 - divisão): "))

if operacao == 1:
    print(soma(num1, num2))
elif operacao == 2:
    print(subtracao(num1, num2))
elif operacao == 3:
    print(multiplicacao(num1, num2))
elif operacao == 4:
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        print(divisão(num1, num2))
else:
    print("Operação inválida. Por favor, escolha uma operação válida (1-4).")

