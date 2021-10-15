while True:
    
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if (x1+x2+y1+y2) == 0:
        break
    if (x1==x2) or (y1==y2):
        if (x1!=x2) or (y1!=y2):
            movimentos = 1
        else:
            movimentos = 0
    elif (abs(x1-x2) == abs(y1-y2)):
        movimentos = 1
    else:
        movimentos = 2
    print(movimentos)    
    