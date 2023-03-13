#Exemplo 7:
#Se a pessoa digitar 1 até 10 = 10%
#Se a pessoa digitar 11 até 20 = 20%
#Se o valor for >21 = 30%

num = int(input("Digite: "))

if(num >= 1 and num <10):
    result = num * 0.1 #acrescentar 10% até 10
    print(result)
elif(num >= 11 and num <= 20):
    result = num * 0.2  #acrescentar 20% até 20
    print(result)
else:
    result = num * 0.3 #acrescentar 30% maior que 21
    print(result)