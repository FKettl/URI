times = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
count = 0

for x in range(15):
    if len(times) == 8:
        count = 0
    if len(times) == 4:
        count = 0
    if len(times) == 2:
        count = 0 
    m, n = [int(x) for x in input().split()]
    if m > n:
        del times[1+count]
        
    elif n > m :
            del times[count]
    count +=1

vencedor = times[0]
print(vencedor)
