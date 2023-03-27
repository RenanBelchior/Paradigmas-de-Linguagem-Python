# k) Faça um programa que peça dois números ao usuário
# e mostre qual o maior e qual o menor.

A = int(input("A: "))
B = int(input("B: "))

if (A > B):
    print(f"{A} é maior e {B} é menor")
elif (A < B):
    print(f"{B} é maior e {A} é menor")
else:
    print("São iguais")