def maybeMonad(fnc):
    def inner(*args):
        for a in args:
            if isinstance(a, Exception):
                return None
        try:
            return fnc(*args)
        except Exception as e:
            return None
    return inner


# 1 Faça um programa que leia 5 números e informe o maior número.

num_list = []

for x in range(0,5):
    num = int(input("Digite o número " + str(x + 1) + ": "))
    num_list.append(num)

response = num_list[0]

for num in num_list:
    if num > response:
        response = num

print("O maior número é " + str(response))


# 2 Faça um programa que leia 5 números e informe a soma e a média dos números.

num_list = []

for x in range(0,5):
    num = int(input("Digite o número " + str(x + 1) + ": "))
    num_list.append(num)

num_sum = 0

for num in num_list:
    num_sum += num

print("A soma de todos os números é: " + str(num_sum))
print("A média dos números é: " + str(num_sum / len(num_list)))


# 3 Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

odd_func = maybeMonad(lambda num : num % 2 != 0)

filtered = filter(odd_func, range(1,51))

for num in filtered:
    print(num)


# 4 Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
# inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
# tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

mult_table = maybeMonad(lambda num: print(str(mult) + " X " + str(num) + " = " + str(mult*num)))

mult = int(input("Digite o multiplo: "))

list(map(mult_table, range(1,11)))


# 5 Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
# usuário. Ex.: 5!=5.4.3.2.1=120

fact = int(input("Digite o número para fazer a conta fatorial: "))

result = 1

for num in range(1, fact + 1):
    result *= num

print(result)


# 6 Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
# seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da
# parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
# 1 0
# 3 10
# 6 15
# 9 20
# 12 25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
# R$ 1.000,00 0 1 R$ 1.000,00
# R$ 1.100,00 100 3 R$ 366,00
# R$ 1.150,00 150 6 R$ 191,67


plans = [
    {"parcels": 1, "tax": 0},
    {"parcels": 3, "tax": 0.1},
    {"parcels": 6, "tax": 0.15},
    {"parcels": 9, "tax": 0.2},
    {"parcels": 12, "tax": 0.25}
]

owed_price = float(input("Valor da dívida: ")) 

print("Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")

table_func = maybeMonad(lambda plan: print("R$ {:.2f} | R$ {:.2f} | {:d} | R$ {:.2f}".format((owed_price * plan["tax"] + owed_price), owed_price * plan["tax"], plan["parcels"], (owed_price * plan["tax"] + owed_price)/plan["parcels"])))

list(map(table_func, plans))


# 7 Faça um programa que mostre os n termos da Série a seguir:
#  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

iterations = int(input("Quantos números deseja observar nesta sequência?: "))

result = 0

for num in range(0, iterations):
     result += (1 + num * 1)/(1 + num * 2)

print(result)


# 8 Mesma letra: Escreva uma função que receba uma string com duas palavras e
# retorne True se ambas palavras começarem com a mesma letra. Exemplo:
# mesma_letra('Cão covarde') -> True
# mesma_letra('Vira Lata') -> False

def checkFirstLetter(text):
    texts = text.lower().split(" ")
    return texts[0][0] == texts[1][0]

checkFirstLetter = maybeMonad(checkFirstLetter)
    
print(checkFirstLetter("Cão covarde"))
print(checkFirstLetter("Vira Lata"))


# 9 Mestre Yoda: Dada uma sentença, a função deve retornar a sentença com as
# palavras na ordem reversa. Exemplo:
# mestre_yoda('Eu estou em casa') --> 'casa em estou Eu'
# mestre_yoda('Estamos prontos') --> 'prontos Estamos'

def mestre_yoda(phrase):
    return " ".join(list(reversed(phrase.lower().split(" ")))).capitalize()

mestre_yoda = maybeMonad(mestre_yoda)

print(mestre_yoda("Eu estou em casa"))
print(mestre_yoda("Estamos prontos"))


# 10 Espião: Escreva uma função que receba uma lista de
# inteiros e retorne True se contém um 007 em ordem, mesmo
# que não contínuo. Exemplo:
# espiao([1,2,4,0,0,7,5]) --> True
# espiao([1,0,2,4,0,5,7]) --> True
# espiao([1,7,2,4,0,5,0]) --> False

def checkSpy(num_list):
    first_zero = False
    second_zero = False
    for num in num_list:
        if second_zero and num == 7:
            return True
        if not second_zero and first_zero and num == 0:
            second_zero = True
        if not first_zero and num == 0:
            first_zero = True
    return False

checkSpy = maybeMonad(checkSpy)

print(checkSpy([1,2,4,0,0,7,5])) 
print(checkSpy([1,0,2,4,0,5,7])) 
print(checkSpy([1,7,2,4,0,5,0]))
