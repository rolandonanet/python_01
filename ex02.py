import re

# 1 - Crie um programa que recebe uma lista de números e

#   - retorne o maior elemento
#   - retorne a soma dos elementos
#    -retorne o número de ocorrências do primeiro elemento da lista
#   - retorne a média dos elementos
#   - retorne o valor mais próximo da média dos elementos
#   - retorne a soma dos elementos com valor negativo
#   - retorne a quantidade de vizinhos iguais

# number_list


number_list = list(map(float,input("Digite uma lista de números entre espaços: ").split()))

avarage = sum(number_list)/len(number_list)

closest_avarage = 0
neighbours = 0

neighbour_iterator = -1

for num in number_list:
    if abs(closest_avarage - avarage) > abs(num - avarage):
        closest_avarage = num
    if (num == number_list[neighbour_iterator] and neighbour_iterator >= 0):
        neighbours += 1
    neighbour_iterator += 1
    


print("O maior valor colocado foi ", max(number_list, key=float))

print("A soma de todos os valores", sum(number_list))
    
print("Primeiro número pareceu: ", number_list.count(number_list[0]), "vezes")

print("A média dos valores é: ", avarage)

print("O valor mais próximo da média é: ", closest_avarage)

print("A soma dos valores em negativo é: ", -sum(number_list))

print("A quantidade de números vizinhos é: ", neighbours)


# 2 - Faça um programa que receba duas listas e retorne True se são iguais ou False caso contrario. 
# Duas listas são iguais se possuem os mesmos valores e na mesma ordem.

first_list = list(map(str,input("Digite a primeira lista separada entre espaços: ").split()))
second_list = list(map(str,input("Digite a primeira lista separada entre espaços: ").split()))

print(first_list == second_list)



# 3 - Faça um programa que receba duas listas e retorne True se têm os mesmos elementos ou False caso contrário Duas listas 
# possuem os mesmos elementos quando são compostas pelos mesmos valores, mas não obrigatoriamente na mesma ordem.

first_list = list(map(str,input("Digite a primeira lista separada entre espaços: ").split()))
second_list = list(map(str,input("Digite a primeira lista separada entre espaços: ").split()))

print(first_list.sort() == second_list.sort())



# 4 - Faça um programa que percorre uma lista com o seguinte formato: 
# [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. 
# Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, 
# no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela:

#   - o total de faltas do campeonato
#   - o time que fez mais faltas
#   - o time que fez menos faltas

soccer_teams = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]


soccer_teams = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]

brasil_faults = soccer_teams[0][2][0] + soccer_teams[1][2][0]
italy_faults = soccer_teams[0][2][1] + soccer_teams[2][2][0]
spain_faults = soccer_teams[1][2][1] + soccer_teams[2][2][1]

faults = brasil_faults + italy_faults + spain_faults

print("O campeonato teve ", faults, "faltas")

if brasil_faults < italy_faults and brasil_faults < spain_faults:
    print("O Brasil cometeu menos faltas")
if italy_faults < brasil_faults and italy_faults < spain_faults:
    print("A Itália cometeu menos faltas")
else: 
    print("A França cometeu menos faltas")

if brasil_faults > italy_faults and brasil_faults > spain_faults:
    print("O Brasil cometeu mais faltas")
if italy_faults > brasil_faults and italy_faults > spain_faults:
    print("A Itália cometeu mais faltas")
else: 
    print("A França cometeu mais faltas")


# 5 - Escreva um programa que conta a quantidade de vogais em uma string e armazena 
# tal quantidade em um dicionário, onde a chave é a vogal considerada.

list_chars = input("Digite uma frase qualquer : ")

vogals = "aeiouAEIOU"

vogal_count = {i: list_chars.count(i) for i in vogals if i in list_chars}

print("A quantidade de cada vogal é: ", vogal_count)


#6 - Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, 
# onde a chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. 
# Escreva uma função que retorna a média do aluno, dado seu nome.

name = "asd"
users = {}

while name != "" :
  name = input("Digite o nome do aluno: ")
  if name != "":
    grades = list(map(float,input("Digite as notas do aluno separado por espaço: ").split()))
    users[name] = grades

print(users)


import random

import random

# 7 - Uma pista de Kart permite 10 voltas para cada um de 6 corredores. 
# Escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor. 
# Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda a classificação final em ordem (1o o campeão).
# O campeão é o que tem a menor média de tempos.

runners = {}

best_lap_time = 99999
best_lap_runner = ""
best_lap = 99
best_avg = 99999
winner = ""

for i in range(6): 
  name = input("Digite o nome do corredor: ")
  laps = []
  for i in range(10):
    lapTime = random.randint(4000, 10000)
    laps.append(lapTime)
    if lapTime < best_lap_time:
      best_lap_time = lapTime
      best_lap_runner = name
      best_lap = i + 1
  if sum(laps) < best_avg:
    best_avg = sum(laps)
    winner = name
  runners[name] = {}
  runners[name]["laps"] = laps
  runners[name]["avg"] = sum(laps)/10

print("Melhor corredor: ", best_lap_runner, "com o tempo de ", best_lap_time, "na volta", best_lap)

sorted_runners = sorted(runners.items(), key = lambda tup: (tup[1]["avg"]))

print(sorted_runners)


for i in range(6): 

  print("O corredor na posição", i + 1, "foi ", sorted_runners[i][0], "com o tempo médio de", sorted_runners[i][1]["avg"])



#8 - Escreva um programa para armazenar uma agenda de telefones em um dicionário. 
#Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. 
#Seu programa deve ter as seguintes funções:

# - incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. 
#Ela deve receber como argumentos o nome e os telefones.
# - incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda. 
#Caso o nome não exista na agenda, você̂ deve perguntar se a pessoa deseja inclui-lo.
#Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome.
# - excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. 
#Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
# - excluirNome – essa função exclui uma pessoa da agenda.
#consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.
option = ""

phonebook = {}

while option != "exit":
  option = input("Oque deseja fazer? IncluirNome(in), IncluirTelefone(it), ExcluirNome(en), ExcluirTelefone(et), consultar(c) ou sair(exit)? ")

  if option == "in":
    name = input("Qual nome deseja incluir?")
    phonebook[name] = []
    number_list = []
    number = ""
    while number != "exit" or len(number_list) < 1:
      number = input("Digite um número para adicionar a este contato (exit para sair)")
      if number != "exit": 
        number_list.append(number)
    phonebook[name] = number_list 
  elif option == "it":
    name = input("Para qual pessoa deseja incluir? ")
    if not name in phonebook: 
      create_option = input("Nome não existente, deseja criar? (y/n) ")
      if create_option == "n":
        next
      phonebook[name] = []
    number = input("Digite um número para adicionar a este contato ")
    phonebook[name].append(number)
  elif option == "et":
    name = input("De qual pessoa deseja deletar o número? ")
    if name in phonebook: 
      number = input("Qual número que deseja remover? ")
      phonebook[name].remove(number)
      if len(phonebook[name]) < 1:
        del phonebook[name]
    else:
      print("Usuário não encontrado")
  elif option == "en":
    name = input("Qual o nome que deseja deletar? ")
    if name in phonebook: 
      del phonebook[name]
    else:
      print("Usuário não encontrado")
  elif option == "c":
    print(phonebook)
  elif option == "exit":
    print("Terminando execução")
  else:
    print("Opção inválida")
    
#   9 - 9 Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
#O arquivo de entrada possui o seguinte formato:
#200.135.80.9
#192.168.1.1
#8.35.67.74
#257.32.4.5
#85.345.1.2
#1.2.3.4
#9.8.234.5
#192.168.0.256
#O arquivo de saída possui o seguinte formato:
#[Endereços válidos:]
#200.135.80.9
#192.168.1.1
#8.35.67.74
#1.2.3.4
#[Endereços inválidos:]
#257.32.4.5
#85.345.1.2
#9.8.234.5
#192.168.0.256

ips = ["200.135.80.9","192.168.1.1","8.35.67.74", "257.32.4.5","85.345.1.2","1.2.3.4","9.8.234.5","192.168.0.256"]

ipsCorretos = ["200.135.80.9","192.168.1.1","8.35.67.74","1.2.3.4"]

ipsIncorretos = ["257.32.4.5","85.345.1.2","9.8.234.5",
"192.168.0.256"]

fileIps = open("ips.txt","w+")

fileResult = open("ipsResult.txt","w+")

for i in ips:
  fileIps.write(i + "%d\r\n")

fileIps.close()

fileResult.write("Ips Corretos")

for x in ipsCorretos:
    fileResult.write(x + "%d\r\n")

fileResult.write("Ips Incorretos")

for z in ipsIncorretos:
    fileResult.write(z + "%d\r\n")

fileResult.close()

contentIps = open("ips.txt","r")

contentResults = open("ipsResult.txt","r")

print(contentIps.readlines())

print(contentResults.readlines())
