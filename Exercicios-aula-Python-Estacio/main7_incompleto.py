# ) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
# calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se
# saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever
# a mensagem 'Saldo Negativo'.


numCliente = int(input('Digite o número do Cliente:'))
saldoCliente = float(input('Digite o saldo do Cliente:'))
debCliente = float(input('Digite o valor do débito do Cliente:'))
credCliente = float(input('Digite o valor do crédito do Cliente:'))

debito = saldoCliente - debCliente
saldoPositivo = saldoCliente > debCliente

if (saldoCliente > debCliente):
    print('Saldo Positivo')


print ('Número da Conta:',numCliente)
print ('Saldo da Conta:',saldoCliente)
print ('Valor do saldo após o débito:',debito)
print ('seu saldo é: ',saldoPositivo)