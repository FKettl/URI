matriz = []
soma = -1
for x in range(3):
    a, b, c = [int(x) for x in input().split()]
    linhas = [a, b, c]
    matriz.append(linhas[:])
for x in range(3):
    if (matriz[x][0] != 0) and (matriz[x][1] !=0) and (matriz[x][2] !=0) and (soma == -1):
            soma = matriz[x][0]+matriz[x][1]+matriz[x][2]
            break
    elif (matriz[0][x] != 0) and (matriz[1][x] !=0) and (matriz[2][x] !=0) and (soma == -1):
        soma = matriz[0][x]+matriz[1][x]+matriz[2][x] 
        break
if soma == -1:
    if (matriz[0][0] !=0) and  (matriz[1][1] != 0) and (matriz[2][2] != 0):
        soma = matriz[0][0] + matriz[1][1] + matriz[2][2]
    elif  (matriz[0][2] != 0) and (matriz[1][1] !=0) and  (matriz[2][0] != 0):
        soma = matriz[0][2] + matriz[1][1] + matriz[2][0]
    elif (matriz[0][2] == 0) and (matriz[1][1] ==0) and  (matriz[2][0] == 0):
        soma = int((matriz[0][1] + matriz[0][0] + matriz[0][1]+ matriz[2][1]+matriz[0][0]+matriz[1][0])/2)
    else:
        soma = int((matriz[0][1] + matriz[0][2] + matriz[0][1]+ matriz[2][1]+matriz[0][2]+matriz[1][2])/2)


for linha in range(3):
    zeros = matriz[linha].count(0)
    count = 0
    for i in range(3):
        if zeros == 1:
            if matriz[linha][i] == 0:
                matriz[linha][i] = abs(soma - matriz[linha][i-1] - matriz[linha][i-2]) 

        elif zeros == 2:
            if matriz[linha][i] == 0:
                if count == 0:
                    if i == 0:
                        if (matriz[linha-1][i] != 0) and (matriz[linha-2][i] !=0):
                            matriz[linha][i] = abs(soma - matriz[linha-1][i] - matriz[linha-2][i])
                        elif (matriz[linha-1][i-1] !=0) and  (matriz[linha-2][i-2] !=0):
                            matriz[linha][i] = abs(soma - matriz[linha-1][i-1] - matriz[linha-2][i-2])
                    elif i == 1:
                        if (linha == 0) and (matriz[1][1] == 0):
                            matriz[1][1] = abs(soma - matriz[0][0] - matriz[2][2])
                            matriz[linha][i] = abs(soma - matriz[linha-1][i] - matriz[linha-2][i])
                        elif (linha == 0) and (matriz[2][1] == 0):
                            matriz[2][1] = abs(soma - matriz[2][0] - matriz[2][2])
                            matriz[linha][i] = abs(soma - matriz[linha-1][i] - matriz[linha-2][i])
                        elif (linha == 1) and (matriz[2][1] == 0):
                            matriz[linha][i] = abs(soma - matriz[0][0] - matriz[2][2])
                        else:
                            matriz[linha][i] = abs(soma - matriz[linha-1][i] - matriz[linha-2][i])

                    count += 1
                elif count == 1:
                    matriz[linha][i] = abs(soma - matriz[linha][i-1] - matriz[linha][i-2])
        

        elif zeros == 3:
            if matriz[linha][i] == 0:
                matriz[linha][i] = abs(soma - matriz[linha-1][i] - matriz[linha-2][i])
        

for linha in range(3):
    print(f'{matriz[linha][0]} {matriz[linha][1]} {matriz[linha][2]}')
                                       
