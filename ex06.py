# 1 Defina a função soma_nat que recebe como argumento um número natural n
# e devolve a soma de todos os números naturais até n.
# Ex: soma_nat(5) = 15

def soma_nat(num):
    if num > 0:
        return num + soma_nat(num - 1)
    return num

assert(soma_nat(5) == 15)


# 2 Defina a função div que recebe como argumentos dois números naturais m
# e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não
# pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão
# inteira.
# Ex: div(7,2) = 3

def div(m, n):
    if (m >= n):
        return 1 + div(m - n, n)
    return 0

assert (div(7,2) == 3)


# 3 Defina a função prim_alg que recebe como argumento um número natural e
# devolve o primeiro algarismo (o mais significativo) na representação decimal de n.
# Ex: prim_alg(5649) = 5
# Ex: prim_alg(7) = 7

def prim_alg(num):
    if(int(num / 10) > 1):
        return prim_alg(num / 10)
    return int(num)

assert (prim_alg(5649) == 5)
assert (prim_alg(7) == 7)


# 4 Defina a função prod_lista que recebe como argumento uma lista de inteiros e
# devolve o produto dos seus elementos.
# Ex: prod_lista([1,2,3,4,5,6]) = 720

def prod_lista(num_list):
    if num_list:
        multi = num_list[0]
        num_list.pop(0)
        return prod_lista(num_list) * multi
    return 1

assert (prod_lista([1,2,3,4,5,6]) == 720)


# 5 Defina a função contem_parQ que recebe como argumento uma lista de números
# inteiros w e devolve True se w contém um número par e False em caso contrário.
# Ex: contem_parQ([2,3,1,2,3,4]) = True
# Ex: contem_parQ([1,3,5,7]) = False

def contem_parQ(num_list):
    if num_list:
        if num_list[0] % 2 == 0:
            return True    
        num_list.pop(0)
        return contem_parQ(num_list)
    return False


assert (contem_parQ([2,3,1,2,3,4]))
assert (not contem_parQ([1,3,5,7]))


# 6 Defina a função todos_imparesQ que recebe como argumento uma lista de
# números inteiros w e devolve True se w contém apenas números ímpares e False
# em caso contrário.
# Ex: todos_imparesQ([1,3,5,7]) = True
# Ex: todos_imparesQ([]) = True
# Ex: todos_imparesQ([1,2,3,4,5]) = False

def todos_imparesQ(num_list):
    if num_list:
        if num_list[0] % 2 == 0:
            return False
        num_list.pop(0)
        return todos_imparesQ(num_list)
    return True


assert (todos_imparesQ([1,3,5,7]))
assert (todos_imparesQ([]))
assert (not todos_imparesQ([1,2,3,4,5]))


# 7 Defina a função pertenceQ que recebe como argumentos uma lista de números
# inteiros w e um número inteiro n e devolve True se n ocorre em w e False em
# caso contrário.
# Ex: pertenceQ([1,2,3],1) = True
# Ex: pertenceQ([1,2,3],2) = True
# Ex: pertenceQ([1,2,3],3) = True
# Ex: pertenceQ([1,2,3],4) = False

def pertenceQ(num_list, num):
    if num_list:
        if num_list[0] == num:
            return True
        num_list.pop(0)
        return pertenceQ(num_list, num)
    return False

assert (pertenceQ([1,2,3],1))
assert (pertenceQ([1,2,3],2))
assert (pertenceQ([1,2,3],3))
assert (not pertenceQ([1,2,3],4))


# 8 Defina a função junta que recebe como argumentos duas listas de números
# inteiros w1 e w2 e devolve a concatenação de w1 com w2 .
# Ex: junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6]
# Ex: junta([],[4,5,6]) = [4, 5, 6]
# Ex: junta([1,2,3],[]) = [1, 2, 3]

def junta(num_list_original, num_list_add):
    if num_list_add:
        num_list_original.append(num_list_add[0])
        num_list_add.pop(0)
        return junta(num_list_original, num_list_add)
    return(num_list_original)


assert (junta([1,2,3],[4,5,6]) == [1,2,3,4,5,6])
assert (junta([],[4,5,6]) == [4,5,6])
assert (junta([1,2,3],[]) == [1,2,3])


# 9 Defina a função temPrimoQ que recebe como argumento uma lista de listas de
# números inteiros w e devolve True se alguma das sublistas w tem um número
# primo e False em caso contrário.
# Ex: temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) = True
# Ex: temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) = False

def temPrimoQ(list_num_list):
    if list_num_list:
        if list_num_list[0]:
            if isPrime(list_num_list[0][0]):
                return True 
            list_num_list[0].pop(0)
            return temPrimoQ(list_num_list)
        list_num_list.pop(0)
        return temPrimoQ(list_num_list)
    return False

def isPrime(num, div = None):
    if div == None:
        div = num - 1
    if num <= 0:
        return False
    if div > 1:
        if num % div == 0:
            return False
        return isPrime(num, div - 1)
    return True

assert (temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]))
assert (not temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]))


# 10 Defina a função inverteLista que recebe como argumento uma lista w e devolve a
# mesma lista mas invertida.
# Ex: inverteLista([1,2,3,4,5]) = [5, 4, 3, 2, 1]
# Ex: inverteLista([])

def inverteLista(num_list):
    if num_list:
        to_add = num_list[0]
        num_list.pop(0)
        if not num_list:
            return [to_add]
        new_list = inverteLista(num_list)
        new_list.append(to_add)
        return new_list
    return num_list

assert (inverteLista([1,2,3,4,5]) == [5,4,3,2,1])
assert (inverteLista([]) == [])
