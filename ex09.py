import asyncio
import time

# 1 Implemente um gerador infinito de números primos.
# Ex:
# i = 0
# while i < 10:
# print(gera_primos())
# i += 1
# Este código imprime os 10 primeiros números primos, isto é: 1, 2, 3, 5, 7, 11, 13, 17,
# 19, 23.

class PrimeIterator:

    def __init__(self, m):
        self.max = m
        self.count = 0
        self.cur = 0


    def __iter__(self):
        return self

    def __next__(self):

        if self.max <= self.count:
            raise StopIteration

        while True:

            self.cur += 1

            divisor = int(self.cur / 2)

            min_divisor = self.cur**0.5

            is_prime = True

            while divisor >= min_divisor and divisor > 1:

                if self.cur % divisor == 0:
                    is_prime = False

                divisor -= 1

            if is_prime:
                self.count += 1
                return self.cur

for prime in PrimeIterator(10):
    print(prime)



# 2 Implementar um gerador que leia um arquivo e retorne uma lista de tuplas com os
# dados (o separador de campo do arquivo é virgula), eliminando as linhas vazias. Caso
# ocorra algum problema, imprima uma mensagem de aviso e encerre o programa.
# Use o exemplo abaixo como arquivo de entrada:
# Ex:
# Entrada:
# teste.txt
# 1,vermelho,2,verde,3,amarelo,4,roxo
# 5,verde,6,preto,7,laranja,8,amarelo
# 9,preto,10,roxo,11,roxo,12,branco
# Chamada:
# gera_tupla(teste.txt)

# Retorno:
# [(1,'vermelho'),(2,'verde'),(3,'amarelo'),(4,'roxo'),(5,'verde
# '),(6,'preto'),(7,'laranja'),(8,'amarelo'),(9,'preto'),(10,'ro
# xo'),(11,'roxo'),(12,'branco')]


class TextIterator:
    def __init__(self, text_file):
        self.text = text_file.read().replace("\n", ",").split(",")
        self.cur_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_pos >= len(self.text):
            raise StopIteration
        
        pos =  self.cur_pos
        self.cur_pos += 2
        return (self.text[pos],self.text[pos + 1])

def gera_tupla(text_file):
    return list(TextIterator(text_file))

text_file = open("teste.txt", "r")

print(gera_tupla(text_file))



# 3 Implementar dois geradores e rodá-los em paralelo (coroutine) para processar dois
# arquivos e gerar tuplas. O primeiro é similar ao do exercício 2. O segundo processa
# outro arquivo, também separado por vírgulas. No final, a lista gerada deve conter
# tuplas com 3 elementos. Use o exemplo baixo como base:
# Entrada:
# teste1.txt
# 1,vermelho,2,verde,3,amarelo,4,roxo
# 5,verde,6,preto,7,laranja,8,amarelo
# 9,preto,10,roxo,11,roxo,12,branco
# teste2.txt
# 0,1,0,0
# 1,1,1,0
# 1,0,0,1

# Chamada:
# gera_tupla1(teste1.txt), gera_tupla2(teste2.txt)
# Retorno:
# [(1,'vermelho',False),(2,'verde',True),(3,'amarelo',False),(4,
# 'roxo',False),(5,'verde',True),(6,'preto',True),(7,'laranja',T
# rue),(8,'amarelo',False),(9,'preto',True),(10,'roxo',False),(1
# 1,'roxo',False),(12,'branco',True)]

class TextIterator:
    def __init__(self, text_file, binary_file):
        self.text = text_file.read().replace("\n", ",").split(",")
        self.binary = binary_file.read().replace("\n", ",").split(",")
        self.cur_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_pos >= len(self.text):
            raise StopIteration
        
        pos =  self.cur_pos
        binary_pos = int(pos/2)
        self.cur_pos += 2
        return (self.text[pos],self.text[pos + 1],  bool(int(self.binary[binary_pos])))

async def readFile(file_name):
    return open(file_name, "r")

async def main():
    task_text = asyncio.create_task(readFile("teste.txt"))
    task_binary = asyncio.create_task(readFile("teste2.txt"))
    await task_text
    await task_binary

    print(list(TextIterator(task_text.result(), task_binary.result())))

asyncio.run(main())


# 4 Escreva um generator que crie um fluxo infinito de inteiros a partir de um valor
# inicial dado com passo 5.
# Ex: gera_inteiros(7) = 12, 17, 22, 27, ...

class MultipleFiveIterator:
    def __init__(self, first):
        self.first = first
    
    def __iter__(self):
        return self

    def __next__(self):
        self.first += 5
        return self.first

for i in MultipleFiveIterator(7):
    print(i)
    # Imeplementei essa quebra para o programa não entrar em loop infinito na exibição
    if i > 25:
        break

# 5 Estenda o generator do exercício 4 em uma coroutine que permita que a mudança
# do passo seja feita de fora (use send()).
# Ex: gera_inteiros_flex(7) = 12, 17, 22, 24, 26, 28, 30...
# Entre 22 e 24 o passo foi alterado de 5 para 2.

def generator(num):
    while True:
        num += yield
        yield num

init_value = int(input("Deseja começar por qual valor? "))

gen = generator(init_value)

iterator = 5

while True:

    next_iterator = input("Qual o valor da proxima iteração? (vazio mantem valor anterior, 'exit' para a operação) ")

    if next_iterator == "exit":
        break
    elif next_iterator != "":
        iterator = int(next_iterator)

    gen.send(None)
    print(gen.send(iterator))
    

