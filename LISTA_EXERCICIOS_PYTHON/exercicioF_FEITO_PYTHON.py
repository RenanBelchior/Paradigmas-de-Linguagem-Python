#f) Escreva um algoritmo para ler o salário mensal atual de um funcionário
# e o percentual de reajuste (aumento). Calcular e escrever o valor do novo salário.

salario = float(input("Salário...: "))
reaj    = float(input("Reajuste %: "))

valor = salario * (reaj / 100)
print(f"Salário Reajustado: {salario + valor}")