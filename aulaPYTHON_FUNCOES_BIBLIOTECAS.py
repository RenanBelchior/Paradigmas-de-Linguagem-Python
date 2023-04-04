#FUNÇÕES, SUBPROGRAMAS E BIBLIOTECAS
1- As *funções* nas ling. de programação tem por objetivo
modularizar códigos bem como organização, ganhando produtividade
de programação

2- As *bibliotecas* reúnem uma série de funções com objetivo
em comum, ou seja, são conjunto de funções
--------------------------------
def imprime():         #DEF: Iniciando uma função | ()Sintaxe da função
    print("Olá mundo") # : delimitação de blocos | Identação do código

imprime()
=================================
#Ex1_de função_PYTHON 1.1
#Envio de parâmetros.
def soma(a, b):    # 8-9 Variáveis locais
    print(a + b)

a = 23             #11-12 variáveis globais
b = 36
soma(a, b)
--------------------------------
#Envio de parâmetros
#Retorno de resultados 1.2
def soma(x, y):    
         x + y

a = 23             
b = 36
resultado = soma(a, b)
print(resultado)
=================================
#Ex_2 de função ANINHAMENTO DE FUNÇÕES
def mult():
    return 2 * 2
    
def soma():    
    resultado = 23 + 36 + mult()
    print(resultado)
    
soma()
===================================
#Ex_3      1.1
#Recursão: procedimento repetitivo para encontrar um resultado.
def imprimir(n):
    if(n == 0):
        return 1
    else:
        print(n)
        return n + imprimir(n - 1)

n = 10  
resultado = imprimir(n)
=======================================
#Ex_4 Recursão
def fatorial(n):
    if(n == 1):
        return 1
    else:
        print(n)
        return n * fatorial(n - 1)

n = 10  
resultado = fatorial(n)
print("Fatorial é: ", resultado)
=======================================
#IMPORTANDO BIBLIOTECAS
#Bilioteca MATH contém funções de matemática
#Ex_1
import math

num = 5.678
print("Teto.........: ", math.ceil(num))
print("Piso.........: ", math.floor(num))
print("Truncamento..: ", math.trunc(num))

num = 5
print("Fatorial.....: ", math.factorial(num))
print("Raiz Quadrada:", math.sqrt(num))
========================================
#Ex_2
import math

x = int(input("x: "))
y = int(input("y: "))
print(f"Potência de {x} elevado a {y}:")
print(math.pow(x, y))

















