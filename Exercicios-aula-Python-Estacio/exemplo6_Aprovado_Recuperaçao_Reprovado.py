#Exemplo 6 Aprovado/Recupração/Reprovado:

nota1 = float(input("Nota 1: "))
nota2 = float(input("nota 2: "))

media = (nota1 + nota2) / 2

if(media >= 6):
    print("Aprovado! =D")
elif (media >= 5):
    print("Recuperação =s")
else:
    print("Reprovado =(")