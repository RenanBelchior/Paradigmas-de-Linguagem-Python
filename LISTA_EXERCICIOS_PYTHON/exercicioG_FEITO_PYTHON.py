# g) Programa em Python que leia o nome de 2 times e o número de gols marcados na partida
# (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser
# impressa a palavra EMPATE.

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
