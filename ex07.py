# 1 Defina a função soma_nat que recebe como argumento um número natural n
# e devolve a soma de todos os números naturais até n.
# Ex: soma_nat(5) = 15

soma_nat = lambda num : num if num == 1 else num + soma_nat(num - 1)

assert(soma_nat(5) == 15)


# 2 Defina a função div que recebe como argumentos dois números naturais m
# e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não
# pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão
# inteira.
# Ex: div(7,2) = 3

div = lambda num, num2 : 0 if num < num2 else 1 + div(num - num2, num2) 

assert(div(7,2) == 3)


# 3 Defina a função prim_alg que recebe como argumento um número natural e
# devolve o primeiro algarismo (o mais significativo) na representação decimal de n.
# Ex: prim_alg(5649) = 5

# Ex: prim_alg(7) = 7

prim_alg = lambda num : int(str(num)[0])

assert(prim_alg(5649) == 5)

assert(prim_alg(7) == 7)


# 4 Defina a função prod_lista que recebe como argumento uma lista de inteiros e
# devolve o produto dos seus elementos.
# Ex: prod_lista([1,2,3,4,5,6]) = 720

prod_lista = lambda num_list : num_list[0] if len(num_list) == 1 else num_list.pop() * prod_lista(num_list)

assert(prod_lista([1,2,3,4,5,6]) == 720)


# 5 Defina a função contem_parQ que recebe como argumento uma lista de números
# inteiros w e devolve True se w contém um número par e False em caso contrário.
# Ex: contem_parQ([2,3,1,2,3,4]) = True
# Ex: contem_parQ([1,3,5,7]) = False

contem_parQ = lambda num_list : False if len(num_list) == 0 else True if num_list.pop() % 2 == 0 else contem_parQ(num_list)

assert(contem_parQ([2,3,1,2,3,4]))
assert(not contem_parQ([1,3,5,7]))


# 6 Defina a função todos_imparesQ que recebe como argumento uma lista de
# números inteiros w e devolve True se w contém apenas números ímpares e False
# em caso contrário.contem_parQ
# Ex: todos_imparesQ([1,3,5,7]) = True
# Ex: todos_imparesQ([]) = True
# Ex: todos_imparesQ([1,2,3,4,5]) = False

todos_imparesQ = lambda num_list : True if len(num_list) == 0 else False if num_list.pop() % 2 == 0 else todos_imparesQ(num_list)

assert(todos_imparesQ([1,3,5,7]))
assert(todos_imparesQ([]))
assert(not todos_imparesQ([1,2,3,4,5]))


# 7 Defina a função pertenceQ que recebe como argumentos uma lista de números
# inteiros w e um número inteiro n e devolve True se n ocorre em w e False em
# caso contrário.
# Ex: pertenceQ([1,2,3],1) = True
# Ex: pertenceQ([1,2,3],2) = True
# Ex: pertenceQ([1,2,3],3) = True
# Ex: pertenceQ([1,2,3],4) = False

pertenceQ = lambda num_list, num : False if len(num_list) == 0 else True if num_list.pop() == num else pertenceQ(num_list, num)

assert(pertenceQ([1,2,3],1))
assert(pertenceQ([1,2,3],2))
assert(pertenceQ([1,2,3],3))
assert(not pertenceQ([1,2,3],4))


# 8 Defina a função junta que recebe como argumentos duas listas de números
# inteiros w1 e w2 e devolve a concatenação de w1 com w2 .
# Ex: junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6]
# Ex: junta([],[4,5,6]) = [4, 5, 6]
# Ex: junta([1,2,3],[]) = [1, 2, 3]

junta = lambda num_list, num_list2 : num_list if len(num_list2) == 0 else junta(num_list, num_list2) if num_list.append(num_list2.pop(0)) == None else None

assert(junta([1,2,3],[4,5,6]) == [1, 2, 3, 4, 5, 6])
assert(junta([],[4,5,6]) == [4, 5, 6])
assert(junta([1,2,3],[]) == [1, 2, 3])


# 9 Defina a função temPrimoQ que recebe como argumento uma lista de listas de
# números inteiros w e devolve True se alguma das sublistas w tem um número
# primo e False em caso contrário.
# Ex: temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) = True
# Ex: temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) = False

checkPrimo = lambda num, num2 = 2 : True if num2 >= num else False if num % (num2) == 0 else checkPrimo(num, num2 + 1)   
temPrimoQ = lambda num_list_list : False if len(num_list_list) == 0 else temPrimoQ(num_list_list) if len(num_list_list[0]) == 0 and not num_list_list.pop(0) == None else True if checkPrimo(num_list_list[0].pop(0)) else temPrimoQ(num_list_list)

assert(temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]))
assert(not temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]))


# 10 Defina a função inverteLista que recebe como argumento uma lista w e devolve a
# mesma lista mas invertida.

# Ex: inverteLista([1,2,3,4,5]) = [5, 4, 3, 2, 1]
# Ex: inverteLista([])

# Não consegui pensar em uma resposta que não precisasse pelo menos instânciar uma variável, sem usar o próprio reverse do python
# inverteLista = lambda num_list : num_list if len(num_list) == 1 else num = num_list.pop(0) , inverteLista(num_list).append(num)

# Resposta temporária, a confirmar com professor
inverteLista = lambda num_list : num_list if num_list.reverse() == None else num_list

assert(inverteLista([1,2,3,4,5]) == [5, 4, 3, 2, 1])
assert(inverteLista([]) == [])
