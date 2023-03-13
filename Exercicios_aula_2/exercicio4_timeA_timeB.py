#4- Leia o numero de gols de dois times, o nome deles e informe se..
#empataram ou qual dos dois ganhou.

timeA = int(input("Digite o numero de gols do Time A: "))
timeB = int(input("Digite o numero de gols do Time B: "))

if (timeA > timeB):
    print("O time A ganhou!")
elif(timeB > timeA):
    print("O Time B ganhou!")
else:
    print("Os 2 times empataram!")
    