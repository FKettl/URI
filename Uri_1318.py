while True:
    count = 0
    falsos = []
    bilhetes, pessoas = [int(x) for x in input().split()]
    if (bilhetes == 0) and (pessoas==0):
        break
        
    serial = [int(x) for x in input().split()]
    serial.sort()
    for x in range(len(serial)):
        if (serial[x] == serial[x-1]) and (serial[x] not in falsos):
            count +=1
            falsos.append(serial[x])
    print(count)

