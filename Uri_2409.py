a, b, c = [int(x) for x in input().split()]
h, l = [int(x) for x in input().split()]
passal = -1
passah = -2
cond1 = 0
cond2 = 0
count = 0

for x in (a, b, c):
    if x <= h :
        passah = x
        cond1 +=1
    if x <= l :
        passal = x
        cond2 +=1

    if passal == passah:
        count += 1
        passal = -1
        passah = -2

if count >= 2 :
    print('S')
elif ((cond2 >= 1) and (cond1 > 1)) or ((cond2 > 1) and (cond1 >= 1)):
    print('S')
elif (cond2 >= 1) and (cond1 >= 1) and (count == 0):
    print('S')
else:
    print('N')


#Com o uso de lista fica mto mais simples porem fiz como uma questão da aula de POO então n podia usar lista.
#Escolhi o uso do for pra tentar diminuir o numero de ifs, ao invés de só fazer direto com varios ifs.