# o) Crie um algoritmo em Python que, dado um número informado 
# pelo usuário, imprima a tabuada dele de 1 a 10. Use o formato de
# apresentação.

num = int(input("Número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {i*num}")