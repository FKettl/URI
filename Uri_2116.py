def isprimo(numero):
    count = 0
    for j in range(1, numero+1):
        if numero % j == 0 :
            count +=1
    if count == 2:
        return True
    else:
        return False

n, m = [int(x) for x in input().split()]

for j in range(n, 0, -1):
    if isprimo(j) == True:
        primo1 = j
        break

for i in range(m, 0, -1):
    if isprimo(i) == True:
        primo2 = i
        break

print(primo1 * primo2)