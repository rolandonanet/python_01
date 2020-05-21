from functools import reduce
from itertools import product
from itertools import dropwhile
from itertools import count
from itertools import combinations
from itertools import permutations
from itertools import groupby
from itertools import cycle
from time import time
from time import sleep
from sys import stdout


# 1 Use map() para criar uma função que encontra o comprimento de cada palavra em
# uma frase (quebrada por espaços) e retorna os valores em um lista. A função deve
# ter como entrada uma string e como saída uma lista de inteiros.
# Ex: word_lengths('How long are the words in this phrase') = [3, 4, 3, 3, 5, 2, 4, 6]

def word_lengths(sentence):
    return list(map(len, sentence.split(" ")))

assert(word_lengths('How long are the words in this phrase') == [3, 4, 3, 3, 5, 2, 4, 6])


# 2 Use reduce() para pegar uma lista de inteiros e retornar o número que
# corresponde à combinação destes dígitos. Por exemplo, [1,2,3] corresponde a cento
# e vinte e três.
# Ex: digits_to_num([3,4,3,2,1]) = 34321

def digits_to_num(num_list):
    return int(reduce(lambda x, y : str(x)+str(y), num_list))

assert(digits_to_num([3,4,3,2,1]) == 34321)


# 3 Use filter() para retornar as palavras de uma lista de palavras que comecem com
# uma determinada letra.
# Ex:
# l = ['hello','are','cat','dog','ham','hi','go','to','heart']
# filter_words(l,'h') = ['hello', 'ham', 'hi', 'heart']

def filter_words(words, char):
    return list(filter(lambda word: word[0] == char, words))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
assert(filter_words(l,'h') == ['hello', 'ham', 'hi', 'heart'])


# 4 Considere uma lista de cartas 'A', '2' .. '10', 'J', 'Q', 'K' e outra lista de naipes: 'P', 'E',
# 'O', 'C' (paus, espadas, ouros e copas). Use itertools.product para criar uma lista com
# todas as combinações de cartas e naipes.
# Ex: ['PA', 'P2', 'P3', ..., 'PQ', 'PK', 'EA', ..., 'CK']
# Ex: concatenate(['A','B'],['a','b'],'-') = ['A-a', 'B-b']

def concatenate(first_list, second_list, separator):
    return list(map(lambda comb: str(comb[0]) + separator + str(comb[1]), list(product(first_list, second_list))))

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suites = ['P', 'E', 'O', 'C']

print(concatenate(suites, cards, ""))
# Exemplo está estranho, um exemplo requer o cartesiano enquanto outro requer combinação um para um
assert(concatenate(['A','B'],['a','b'],'-') == ['A-a', 'A-b', 'B-a', 'B-b'])


# 5 Use itertools.cycle para criar um spinner (a antiga ampulheta do windows) no
# formato caractere. Use os caracteres \|/– para simular a rotação. A função spinner
# recebe como parâmetro o tempo de duração do spinner. Use time.time() para o
# tempo, sys.stdout.write() para escrever o caractere do spinner, sys.stdout.flush()
# para disparar a thread e time.sleep() para reduzir a velocidade de rotação.

def spinner(duration, time_betwen_ticks):

    target_time = time() + duration

    for tick in cycle(['\\', '|', '/', '–']):

        sleep(time_betwen_ticks)

        stdout.write(tick)
        stdout.flush()

        if time() >= target_time:
            break

spinner(2, 0.1)


# 6 Dado um dicionário cujas chaves sejam nomes de livros e seus respectivos valores
# sejam suas quantidades em estoque, use itertools.dropwhile para retornar livros
# com quantidade maior ou igual a 2.

books = {
    "Hardy Woody": 100,
    "Hairy Potter": 1,
    "Cancer": 2,
    "In kink we trust": -1
}

def getBooksWithEqualOrMoreThan(books, ammount):
    return list(dropwhile(lambda book: books[book] >= ammount, books.keys()))

print(getBooksWithEqualOrMoreThan(books, 2))


# 7 Dada uma lista de alunos, quantos pares podem ser formados? Use
# itertools.combinations.

students = ["Jorge", "Pablo", "Aquela tia", "Teófila"]

def studentCount(students):
    return len(list(combinations(students, r=2)))

print(studentCount(students))


# 8 Quantas palavras de 4 letras podem ser formadas a partir de uma lista de 7 letras.
# Use itertools.permutations.

def wordPermutations(char_list):
    return len(list(permutations(char_list, 4)))

print(wordPermutations(['1', '2', '3', '4', '5', '6', '7']))


# 9 Considere um dicionário cuja chave são nomes de usuários e os respectivos valores
# são o meio de contato preferido (opções: e-mail, carta, whatsapp, telefone fixo, fax e
# celular).
# Crie uma função que retorna a quantidade de usuários que preferem e-mail. Use
# itertools.groupby().

users = {
    "Pablo" : "e-mail",
    "Josepha": "carta",
    "Rhoserbaldo": "whatsapp",
    "Herisvaldo": "telefone fixo",
    "Draxion": "fax",
    "Bênis": "celular" ,
    "Néju" : "e-mail",
    "Zherihio": "carta",
    "Vitoriano": "whatsapp",
    "Cara" : "e-mail"
}

def countEmailUsers(users):
    users = {k: v for k, v in sorted(users.items(), key=lambda item: item[1])}

    for key, group in groupby(users.keys(), lambda user_name: users[user_name]):
        if key == "e-mail":
            return len(list(group))
    return 0

print(countEmailUsers(users))

