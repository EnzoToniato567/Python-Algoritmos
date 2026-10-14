# Escreve um algoritmo que solicita 3 lados de um triângulo e verifica se ele é equilátero, isósceles ou escaleno

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 == lado2 and lado1 == lado3:
    print("O triângulo é equilátero. Possue todos os lados iguais.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles. Possue dois lados iguais.")
else:
    print("O triângulo é escaleno. Possue todos os lados diferentes.")