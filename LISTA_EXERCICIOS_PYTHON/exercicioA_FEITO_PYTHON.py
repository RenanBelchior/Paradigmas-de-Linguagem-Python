#a) Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. 
# Sabendose que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5%
# sobre o que ultrapassar este valor, calcular e escrever o seu salário total. 

salario = int(input("Digite o Salário: "))
venda = int(input("Digite o valor das vendas: "))

salarioTotal = salario + venda
comissao = salarioTotal * 0.5
comissao2 = salarioTotal * 0.3

if (venda > 1500):
    result = venda + comissao * 0.5
    print("Vendas acima de 1.500.00! Seu salário será: ", result)
elif (venda < 1500):
    result = venda + comissao2 * 0.3
    print("Venda abaixo de 1.500.00! Seu salario será: ", result)
else:
    print("Não vendeu um peixinho! :(")