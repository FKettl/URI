while True:
    try:
        n, r = [int(x) for x in input().split()]
        foram = [x for x in range(1, n+1)]
        voltaram = [int(x) for x in input().split()]
        naoVoltaram = [x for x in range(1, n+1) if x not in voltaram]
        
        if not naoVoltaram:
            print('*')
        
        else:
            for j in range(len(naoVoltaram)):
                print(f'{naoVoltaram[j]} ', end='')
            print('')  

    except EOFError:
        break
