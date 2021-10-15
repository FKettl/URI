n = int(input())
total = 0
antes = -10
for x in range (n):
    instante = int(input())
    if instante < (antes+10):
        total += (instante - antes)
    else:
        total +=10
    antes = instante
print(total)    
