Tipo de dados primitivos:
int, str, float.

Tipo de Dados Aglomerados:
Listas - agrupar um conjunto de elementos.
Tuplas - semelhante a lista, porém imutável.
Dicionários - agrupar elementos vão ser recuperados por uma chave.
Sets - ????
-------------------------------------------------------------------------------------------
. definição de uma lista:
lista = ['python', 'a', 15, 2]
lista.append(89) "insere elemento ao final da lista"
lista.insert(3, 89) "adiciona elemento porém escolhe qual posição será inserido"
print(lista)
-------------------------------------------------------------------------------------------
. definição de uma lista com teclado
lista = ['python', 'a', 15, 2]

num = int(input("Elemento: "))
index = int(input("Posição: "))

lista.insert(index, num)
print(lista)
-------------------------------------------------------------------------------------------
. definição de uma lista com estrutura de repetição
lista = ['python', 'a', 15, 2]

for i in lista:
        print(i)

print(i)
-------------------------------------------------------------------------------------------
. definição de lista com concatenação
lista = ['python', 'a', 15, 2]
lista1 = [5, 35]

print(lista + lista1)
-------------------------------------------------------------------------------------------
. definição de lista para averiguar se há tipo dentro da lista ou não (true/false)
lista = ['python', 'a', 15, 2]
lista1 = [5, 35]

print("Tem python na lista: ", "Python" in lista)
-------------------------------------------------------------------------------------------
. definição de lista para ver o maximo e o minimo da lista
lista1 = [5, 35, 23, 77, 12, 84, 21]

print("Máximo: ", max(lista1))
print("Mínimo: ", min(lista1))
-------------------------------------------------------------------------------------------
. definição de lista para somar o que há na lista
lista1 = [5, 35, 23, 77, 12, 84, 21]

print("Soma: ", sum(lista1))
-------------------------------------------------------------------------------------------
. definição para saber a quantidade de elementos da lista de forma númerico
lista1 = [5, 35, 23, 77, 12, 84, 21]

print("Qtde elementos: ", len(lista1))
-------------------------------------------------------------------------------------------
. definição de lista para deletar o elemento.
lista1 = [5, 35, 23, 77, 12, 84, 21]

list.pop(2)
print(lista1)
-------------------------------------------------------------------------------------------
. ordena de forma alfabética as palavras.
ListaFrutas = ["maça", "uva", "banana", "pera"]

ListaFrutas.sort()

print(ListaFrutas)
-------------------------------------------------------------------------------------------
TUPLAS !!!!!!!!!!!!
NÃO PODE INSERIR, DELETAR, ALTERAR.. PODE APENAS CONSULTAR.
É delimitado por ().

-------------------------------------------------------------------------------------------
SET'S !!!!!!!!!!!!!!!
É UMA LISTA, PORÉM NÃO POSSUI ORDENAÇÃO ESPECÍFICA DOS DADOS.
ELE PODE EXCLUIR ELEMENTOS REPETITIVOS DA LISTA.
{2, 57, 57, 3, 9}

DELIMITADOS POR CHAVES {}

-------------------------------------------------------------------------------------------
DICIONARIOS !!!!!!!!!!!!!!!!!!!!!!!
DELIMITADOS POR CHAVES {}

dicionario={'aaa':10,'bbb':15,'ccc':20}
lista1 = {1:"nome1", 2:"nome2", 3:"nome3"}
qtde_frutas={'pera':10, 'maça':15, 'uva':20}
-------------------------------------------------------------------------------------------
. PASSAR O VALOR PELO INDICE DO DICIONARIO.
qtde_frutas = {"uva":10, "pera":15, "maçã":20}

qtde_frutas["banana"] = 5

print(qtde_frutas)
-------------------------------------------------------------------------------------------
Acessando os elementos do dicionário com os métodos keys(),
items() e values():
Acessando dados.

qtde_frutas = {'pera': 10, 'uva': 15,'maçã': 20}

print(qtde_frutas.keys())
print(qtde_frutas.items())
print(qtde_frutas.values())
-------------------------------------------------------------------------------------------
Iterando sobre os elementos do dicionário com os métodos
keys(), items() e values():
Dicionários em Python: Acessando dados

qtde_frutas = {'pera': 10, 'uva': 15,'maçã': 20}
for i in qtde_frutas.keys():
  print(i)
-------------------------------------------------------------------------------------------
. Removendo valores nos dicionários com o método del():

qtde_frutas = {'pera': 10, 'uva': 15,'maçã': 20}
print(qtde_frutas)
del qtde_frutas['uva']
print(qtde_frutas)

Vai imprimir:
{'pera': 10, 'uva': 15, 'maçã': 20}
{'pera': 10, 'maçã': 20}
----------------------------------------------------------------------------------
Removendo com o método pop().
Além de remover o elemento com a chave especificada do dicionário,
ele retorna o valor desse elemento. Também podemos definir um valor
padrão de retorno, para caso a chave não seja encontrada:

qtde_frutas = {'pera': 10, 'uva': 15,'maçã': 20}
print(qtde_frutas.pop('maçã', 'Elemento não encontrado'))
print(qtde_frutas.pop('banana', 'Elemento não encontrado'))
Vai imprimir: 20
Elemento não encontrado
----------------------------------------------------------------------------------
EXERCICIO
#Questão 01: Desenvolva um programa que tendo uma lista de
#inteiros, retorne o maior número dessa lista.
#lista = [2,3,4,1,4,6,3,7,54,4,1]

#print("Maior número:",max(lista))


#Questão 02: Desenvolva um programa que tendo uma lista de
#inteiros repetidos, retorne uma nova lista eliminando elementos
#duplicados.
#a = {1,1,1,2,3,4,5,6,7,8,8,9,10}

#print(a)


#Questão 03: Seja a seguinte tupla: exe_tupla = ("Orange",
#[10, 20, 30], (5, 15, 25)), imprima na tela o número 20,
#acessando pelo índice/endereço dela.























