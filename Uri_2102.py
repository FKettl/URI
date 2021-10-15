n = int(input())
for y in range(n):
    matriz = {}
    inutil1, entradas = [int(x) for x in input().split()]
    for x in range(entradas):
        inutil2, linha, coluna, valor =input().split()
        valor = int(valor)
        if (linha, coluna) in matriz:
            matriz[linha, coluna] += valor
        else:
            matriz[linha, coluna] = valor
    indice = sorted(matriz.keys())
    
    for x in indice:
        print(f'{x[0]} {x[1]} {matriz[x]}')

    if y != (n-1):
        print()
    else:
        break

