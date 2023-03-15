#6- Leia as opções de um usuario e dois numeros reais e..
#faça os seguintes calculos, de acordo com a escolha..
#do usuario.
# 1-Soma dos numeros
# 2-Subtraia os numeros
# 3-Multiplica os numeros

num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
print("\n")
print ("Digite + para ver a soma")
print ("Digite - para ver a subtração")
print ("Digite * para ver a mulitplicação")
escolha = input("Digite a sua escolha: ")
print("\n")
if (escolha == "+"):
    resultado = num1 + num2
elif (escolha == "-"):
    resultado = num1 - num2
elif (escolha == "*"):
    resultado = num1 * num2
else:
    print("Nenhuma operação escolhida!")
    resultado = 0
    
print("Resultado: ", resultado)