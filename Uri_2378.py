n, c = [int(x) for x in input().split()]
total = 0
excedeu = False
 
for i in range(n):
    s, e = [int(x) for x in input().split()]
    total -= s
    total += e
    if total > c:
        excedeu = True
    
if excedeu == True:
    print('S')
else:
    print('N')