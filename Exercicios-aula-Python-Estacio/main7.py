# ) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
# calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se
# saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever
# a mensagem 'Saldo Negativo'.


numCliente = int(input('Informe o Número do Cliente:'))
saldoCliente = float(input('Informe o Saldo do Cliente:'))
debCliente = float(input('Informe o Valor do débito do Cliente:'))
credCliente = float(input('Informe o Valor do crédito do Cliente:'))


saldoAtual = saldoCliente - debCliente + credCliente


print ('Número da Conta:',numCliente)
print ('Saldo da Conta:',saldoCliente)
print ('Valor do saldo após o débito:',saldoAtual)


if saldoAtual >= debCliente:
    print ('O seu Saldo é Positivo')
else:
    print('O seu Saldo é negativo')
