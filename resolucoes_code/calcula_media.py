# Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 

teste= 0
soma = 0

while teste < 3:
    nota = float(input("Digite a nota do aluno: "))
    teste +=1
    soma += nota

print(f"A média do(a) aluno(a) é {soma / 3}")