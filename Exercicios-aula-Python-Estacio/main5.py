# e) Faça um Programa Python que peça 2 números inteiros e um número real. Calcule e
# mostre:
# a. o produto do dobro do primeiro com metade do segundo
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo

num1 = int(input('Digite o primeiro numero: '))
num2 = int (input('Digite o segundo número: '))
num3 = float(input('Digite um valor real: '))

a = num1 * 2
a1 = num2 / 2

b = num1 + num1 + num1 + num3

c = num3**3

print ('O produto dobro do primeiro número: ',a)
print ('A metade do segundo número é: ',a1)
print ('A soma triplo do primeiro número com o terceiro é: ', b)
print ('O valor real elevado ao cubo é: ',c)