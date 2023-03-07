# b) Ler o nome e o salário fixo de um funcionário e calcular 10% de aumento e mostrar o
# resultado do salário aumentado.

pessoa = (input('Digite o nome do funcionário(a): '))
salario = float(input('Digite o Salário do funcionário(a): '))

if (salario <= 100.0):
 porcentual = 10
else:
 porcentual = 5

porcentual = porcentual/100.0
aumento = porcentual * salario
novoSalario = salario + aumento

print ('Funcionario:', pessoa)
print ('Salário: ', salario)
print ('Salário aumentado em 10%: ',novoSalario)
