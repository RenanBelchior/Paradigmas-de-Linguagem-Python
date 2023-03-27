# q) Faça um script em Python que imprima na tela os 
# múltiplos de 5 entre 1 e 100 e a quantidade desses números.

conta = 0
for i in range(1, 101):
    if(i % 5 == 0):
        print(f"{i} é múltiplo de 5.")
        conta = conta + 1
print(f"Qtde de múltiplos 5: {conta}")