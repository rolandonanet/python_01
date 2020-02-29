import math
import calendar
import random


# 1- Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
radius = float(input("Qual o raio do círculo em metros? "))
print("A área deste círculo é %.2fm²" %(math.pi*(radius**2)))


# 2- Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
length = float(input("Qual o tamanho do lado do quadrado em metros? "))
print("A área deste quadrado é %.2fm²" %(length**2))
print("O dobro da área deste quadrado é %.2fm²" %(2*length**2))


#3 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
money = float(input("Quanto ganha por hora? "))
hours = float(input("Quantas horas trabalha por mês? "))
print("O seu salário é de R$%.2f" %(money*hours))


# 4 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
temperature = float(input("Qual a temperatura em Farenheit? "))
print("A temperatura em Celsius seria %.2f°C" %(5*(temperature-32)/9))


# 5 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
temperature = float(input("Qual a temperatura em Celsius? "))
print("A temperatura em Farenheit seria %.2f°F" %(9*temperature/5+32))


# 6 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# - o produto do dobro do primeiro com metade do segundo .
# - a soma do triplo do primeiro com o terceiro.
# - o terceiro elevado ao cubo.
first = int(input("Digite primeiro número inteiro: "))
second = int(input("Digite Segundo número inteiro: "))
third = float(input("Digite um número real: "))

print("Produto do dobro do primeiro com metade do segundo: %.2f" %(first*2 * second/2))
print("Soma do triplo do primeiro com o terceiro: %.2f" %(first*3 + third))
print("Terceiro elevado ao cubo: %.2f" %(third**3))


# 7 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#  Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
#  deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
#  e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
#  Caso contrário mostrar tais variáveis com o conteúdo ZERO.
max_weight = 50
weight = float(input("Qual o peso do peixe? "))
tax = 0
if weight > max_weight:
    tax = (weight - max_weight)*4
    print("Passou do limite de peso, multa será de R$%.2f" %tax)
else:
    print("Não passou do peso limite, não haverá multa")


# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o indicato, faça um programa que nos dê:

# - salário bruto.
# - quanto pagou ao INSS.
# - quanto pagou ao sindicato.
# - o salário líquido.
# - calcule os descontos e o salário líquido, conforme a tabela abaixo:
#     - Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     - Salário Liquido : R$ 
# Obs.: Salário Bruto - Descontos = Salário Líquido.

money = float(input("Quanto ganha por hora? "))
hours = float(input("Quantas horas trabalha por mês? "))
net_salary = money*hours
earnings_tax = 0.11
inss_tax = 0.08
syndicate_tax = 0.05

print("O seu salário bruto é de R$%.2f" %net_salary)
print("O valor pago ao INSS é de R$%.2f" %(net_salary * inss_tax))
print("O valor pago ao sindicato é de R$%.2f" %(net_salary * syndicate_tax))
print("O seu salário líquido é de R$%.2f" %(net_salary * (1 - earnings_tax - inss_tax - syndicate_tax)))


# 9 - Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo. 
# Exemplo: String 1: Brasil Hexa 2018 String 2: Brasil! Hexa 2018! 
# Tamanho de "Brasil Hexa 2018": 16 caracteres Tamanho de "Brasil! Hexa 2018!": 18 caracteres 
# As duas strings são de tamanhos diferentes. As duas strings possuem conteúdo diferente.

first = input("Digite a primeira palavra: ")
second = input("Digite a segunda palavra: ")

first_size = len(first)
second_size = len(second)

print("A primeira palavra '{0}' possui {1} caractéres".format(first, first_size))
print("A Segunda palavra '{0}' possui {1} caractéres".format(second, second_size))

if first == second:
    print("As duas palavras são iguais")
elif first_size == second_size:
    print("As duas palavras são diferentes, mas possuem o mesmo tamanho")
else:
    print("As duas palavras são diferentes e possuem tamanhos diferentes")


# 10 - Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre
#  o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas. Observação: não use loops.
name = input("Digite seu nome: ")
print("O seu nome ao contrário em letras maiúsculas seria %s" %name[::-1].upper())


# 11 - Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
# Data de Nascimento: 29/10/1973 Você nasceu em 29 de Outubro de 1973. Obs.: Não use desvio condicional nem loops.

mes_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio',  6: 'junho',  7: 'julho',  8: 'agosto',  9: 'setembro',  10: 'outubro',  11: 'novembro',  12: 'dezembro'}
birth_date = input("Digite sua data de nascimento (dd/mm/aaaa): ")
day = birth_date[:2]
month = birth_date[3:5]
month_name = mes_ext[int(month)]
year = birth_date[6:len(birth_date)]

print("Você nasceu em {} de {} de {}".format(day, month_name, year))


# 12 - Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, 
# como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. 
# O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, 
# sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. 
# Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o 
# para a grafia leet speak. Desafio: não use loops nem desvios condicionais.

text = input("Digite um texto para traduzir para Leet: ")

alphabet = {
    "a":["4","@"],
    "b":["8", "ß"],
    "c":['[', '¢', '<', '('],
    "d":['|)', '|o', '[)', 'I>', '|>'],
    "e":['3', '&', '£', 'ë', '€', 'ê'],
    "f":['|=', 'ph', '|#'],
    "g":['6', '9'],
    "h":['/-/', '[-]', '{=}', '<~>', '|-|'],
    "i":['1', '!', '|'],
    "j":['_/'],
    "k":['|<', '|{', ']{', '}<', '|('],
    "l":["1_", '|_'],
    "m":['|v|', '[V]', '{V}', '(u)', '(V)', 'IVI'],
    "n":["/|/"],
    "o":["0"],
    "p":['|^', '|*', '|o', '|>', '|"', ']D', '|°', '|7'],
    "q":['q', '9'],
    "r":['|2', '|?', 'lz', '[z', '12'],
    "s":['5', '$', 'z', '§'],
    "t":["'|'", '"|"'],
    "u":['(_)', '|_|'],
    "v":["v",'u','V'],
    "w":['(n)', "v'v"],
    "x":['><'],
    "y":['Y', 'j', '¥'],
    "z":['2', 'z', '%']
}
a = str(random.sample(alphabet["a"], k=1)[0])
b = str(random.sample(alphabet["b"], k=1)[0])
c = str(random.sample(alphabet["c"], k=1)[0])
d = str(random.sample(alphabet["d"], k=1)[0])
e = str(random.sample(alphabet["e"], k=1)[0])
f = str(random.sample(alphabet["f"], k=1)[0])
g = str(random.sample(alphabet["g"], k=1)[0])
h = str(random.sample(alphabet["h"], k=1)[0])
i = str(random.sample(alphabet["i"], k=1)[0])
j = str(random.sample(alphabet["j"], k=1)[0])
k = str(random.sample(alphabet["k"], k=1)[0])
l = str(random.sample(alphabet["l"], k=1)[0])
m = str(random.sample(alphabet["m"], k=1)[0])
n = str(random.sample(alphabet["n"], k=1)[0])
o = str(random.sample(alphabet["o"], k=1)[0])
p = str(random.sample(alphabet["p"], k=1)[0])
q = str(random.sample(alphabet["q"], k=1)[0])
r = str(random.sample(alphabet["r"], k=1)[0])
s = str(random.sample(alphabet["s"], k=1)[0])
t = str(random.sample(alphabet["t"], k=1)[0])
u = str(random.sample(alphabet["u"], k=1)[0])
v = str(random.sample(alphabet["v"], k=1)[0])
w = str(random.sample(alphabet["w"], k=1)[0])
x = str(random.sample(alphabet["x"], k=1)[0])
y = str(random.sample(alphabet["y"], k=1)[0])
z = str(random.sample(alphabet["z"], k=1)[0])
text = text.replace("a", a)
text = text.replace("b", b)
text = text.replace("c", c)
text = text.replace("d", d)
text = text.replace("e", e)
text = text.replace("f", f)
text = text.replace("g", g)
text = text.replace("h", h)
text = text.replace("i", i)
text = text.replace("j", j)
text = text.replace("k", k)
text = text.replace("l", l)
text = text.replace("m", m)
text = text.replace("n", n)
text = text.replace("o", o)
text = text.replace("p", p)
text = text.replace("q", q)
text = text.replace("r", r)
text = text.replace("s", s)
text = text.replace("t", t)
text = text.replace("u", u)
text = text.replace("v", v)
text = text.replace("w", w)
text = text.replace("x", x)
text = text.replace("y", y)
text = text.replace("z", z)

print ("O texto em leet speak ficaria: %s" %text)


