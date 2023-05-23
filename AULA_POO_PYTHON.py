#EXEMPLO DE POO em Python
#Classe pessoa, nome, idade, peso.
#Método: andar e dormir

#EXEMPLO DE CRIAÇÃO DE CLASSE COM CARACTERISTICAS
#class Pessoa():
#    pass

#pessoa1 = Pessoa()
#pessoa1.nome = "Juliana"
#pessoa1.idade = 23
#pessoa1.peso = 75
#print(pessoa1.nome, pessoa1.idade, pessoa1.peso)

#pessoa2 = Pessoa()
#pessoa2.nome = "Carlos"
#pessoa2.idade = 22
#pessoa2.peso = 61
#print(pessoa2.nome, pessoa2.idade, pessoa2.peso)
#------------------------------------------------------------------------------

#EXEMPLO 1 COM CONSTRUTOR __init__ e self.
#class Pessoa():
#    def __init__(self):
#        self.nome = "Juliana"
#        self.idade = 28
#        self.peso = 75

#pessoa1 = Pessoa()
#print(pessoa1.nome, pessoa1.idade, pessoa1.peso)
#------------------------------------------------------------------------------

#EXEMPLO 1.2
#class Pessoa(object):
#    def __init__(self, nome, idade, peso):
#        self.nome = nome
#        self.idade = idade
#        self.peso = peso

#pessoa1 = Pessoa("Juliana", 23, 65)
#pessoa2 = Pessoa("Carlos", 22, 69)
#print(pessoa1.nome, pessoa1.idade, pessoa1.peso)
#print(pessoa2.nome, pessoa2.idade, pessoa2.peso)
#------------------------------------------------------------------------------

#EXEMPLO 1.3 METODOS E COMPORTAMENTOS
#class Pessoa(object):
#    def __init__(self, nome, idade, peso):
#        self.nome = nome
#        self.idade = idade
#        self.peso = peso
#    def andar(self): #metodo andar
#        print("O ser humano é mamífero que anda")

#pessoa1 = Pessoa("Juliana", 22, 65)
#pessoa2 = Pessoa("Carlos", 22, 69)
#pessoa1.andar()
#pessoa2.andar()
#------------------------------------------------------------------------------

#EXEMPLO 2 CALCULADORA

#class Calculadora:
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b
        
#    def soma(self):
#        return self.a + self.b
    
#    def subtrai(self):
#        return self.a - self.b
    
#    def multiplicar(self):
#        return self.a * self.b
    
#    def divide(self):
#        return self.a / self.b


#c = Calculadora(150, 2)
#print("soma: ", c.soma())
#print("subtração: ", c.subtrai())
#print("multiplicação: ", c.multiplicar())
#print("divisão: ", c.divide())
#------------------------------------------------------------------------------

#EXEMPLO 3 CONTA BANCARIA

#class Conta():
#    def __init__(self, numero, cpf, nomeTitular, saldo):
#        self.numero = numero
#        self.cpf = cpf
#        self.nomeTitular = nomeTitular
#        self.saldo = saldo
        
#    def depositar(self, valor):
#        self.saldo += valor
    
#    def sacar(self, valor):
#        if(self.saldo < valor):
#            return False
#        else:
#            self.saldo -= valor
#           return True
            
#    def gerar_extrato(self):
#        print(f"numero: {self.numero}\n cpf: {self.cpf}\n saldo: {self.saldo}")

#    def main():
#        c1 = Conta(1, 1, "Joao",0)
#        c1.depositar = (300)
#        saque = c1.sacar(400)
#        c1.gerar_extrato()
#        print(f"O saque foi realizado? {saque}")
    
#    if (__name__ == "__main__"):
#        main()
#------------------------------------------------------------------------------

#CLASSE HERANÇA EXEMPLO 1 !!!!!!!!!

#class Pessoa(object):
#    def __init__(self, nome, cpf, ano):
#        self.nome = nome
#        self.cpf = cpf
#        self.ano_nasc = ano

#class Aluno(Pessoa):                      #SUBCLASSE aluno
#    def __init__(self, nome, cpf, ano):
#        super().__init__(nome, cpf, ano)

#class Professor(Pessoa):                  #SUBCLASSE professor
#    def __init__(self, nome, cpf, ano):
#        super().__init__(nome, cpf, ano)

#aluno1 = Aluno("Juliana", 111333223322, 1995)
#print(aluno1.nome, aluno1.cpf, aluno1.ano_nasc)

#professor1 = Professor("Rogerio", 1211231231, 1994)
#print(professor1.nome, professor1.cpf, professor1.ano_nasc)
#------------------------------------------------------------------------------

#POLIMORFISMO !!!!!!!!!!
#class Mamiferos():
#    def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#    def locomover(self):
#        print("teste")
    
#class MicoLeao(Mamiferos):
#    def __init__(self, nome, idade):
#        super().__init__(nome, idade)
    
#    def locomover(self):
#        print("Pular galhos")

#class Humano(Mamiferos):
#    def __init__(self, nome, idade):
#        super().__init__(nome, idade)
    
#    def locomover(self):
#        print("Andar")
        
#class Baleia(Mamiferos):
#    def __init__(self, nome, idade):
#        super().__init__(nome, idade)
    
#    def locomover(self):
#        print("Nadar")

#animal = Humano("sofia", 20)
#print(animal.nome, animal.idade)
#animal.locomover()
#------------------------------------------------------------------------------

#EXERCICIO !!!!!!!!!

#class Funcionario():
#    def __init__(self, nome, matricula):
#        self.nome = nome
#        self.matricula = matricula

#class Gerente(Funcionario):
#    def __init__(self, nome, matricula):
#        super().__init__(nome, matricula)
    
#    def salario(self):
#        print("Salario 9.000")

#class Diretor(Funcionario):
#    def __init__(self, nome, matricula):
#        super().__init__(nome, matricula)
    
#    def salario(self):
#        print("Salario 5.500")

#class Secretario(Funcionario):
#    def __init__(self, nome, matricula):
#        super().__init__(nome, matricula)
    
#    def salario(self):
#        print("Salario 3.500")

#class Presidente(Funcionario):
#    def __init__(self, nome, matricula):
#        super().__init__(nome, matricula)
    
#    def salario(self):
#        print("Salario 20.000")

#funcionario = Secretario("Fernando", 1122)
#print(funcionario.nome, funcionario.matricula)
#funcionario.salario()







