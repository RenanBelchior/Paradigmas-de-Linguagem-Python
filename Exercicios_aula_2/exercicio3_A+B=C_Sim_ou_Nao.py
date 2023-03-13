#Exercicio 3: Leia os valor A,B,C e verifique se a soma de A + B
# é igual a C

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int (input("Digite o valor C: "))

soma = a + b

if (soma == c):
    print("A soma é igual a C")
else:
    print("A soma não é igual a C")