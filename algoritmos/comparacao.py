# Escreve um algoritmo que imprime o maior de dois números e verifica se eles são iguais

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O número maior é: ", num1)
elif num1 < num2:
    print("O número maior é: ", num2)
else: 
    print("Os números são iguais")