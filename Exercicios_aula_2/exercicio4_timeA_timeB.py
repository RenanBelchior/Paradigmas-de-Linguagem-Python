#4- Leia o numero de gols de dois times, o nome deles e informe se..
#empataram ou qual dos dois ganhou.

timea = (input("Digite o nome do time A: "))
timeb = (input("Digite o nome do time B: "))
timeA = int(input("Digite o numero de gols do Time A: "))
timeB = int(input("Digite o numero de gols do Time B: "))

if (timeA > timeB):
    print("O time",timea ,"ganhou!")
elif(timeB > timeA):
    print("O time",timeb ,"ganhou!")
else:
    print("O time",timea ,"e", timeb ,"empataram!")
