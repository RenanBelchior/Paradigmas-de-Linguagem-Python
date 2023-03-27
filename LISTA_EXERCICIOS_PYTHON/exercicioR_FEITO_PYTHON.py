# r) Desenvolva um código em Python que calcule a média aritmética 
# entre 1 e 20.

soma = 0
cont = 0
for i in range(1, 21):
    soma = soma + i
    cont = cont + 1
    
print(f"Média de 1..20: {soma / cont}")