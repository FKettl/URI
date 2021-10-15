 
while True:
    numcomandos = int(input())
    if numcomandos == 0:
        break
    count = 0
    total = 0
    comandos = [int(x) for x in input().split()]
    novocomandos = []
    for x in comandos:
        if x in novocomandos:
            total += novocomandos.index(x)+1            
        else:
            total += x+count
        count += 1
        novocomandos.insert(0, x)
    print(total)
    
