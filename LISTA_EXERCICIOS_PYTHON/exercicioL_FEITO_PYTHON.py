# l) Para doar sangue é necessário ter entre 18 e 67 anos. Faça um aplicativo na linguagem
# Python que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.

print("=== Verificador de idades para Doar Sangue ===\n")
idade = int(input("Digite a sua idade: "))

if (idade > 17 and idade <= 67):
    print("Você pode ser um doador(a) de sangue! =D")
else:
    print("Você não está apto(a) para ser um doador(a) =(")
