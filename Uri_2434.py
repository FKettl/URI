n, movido = [int(x) for x in input().split()]
total = movido
menor = total
for j in range(n):
    movido = int(input())
    total += movido
    if total < menor:
        menor = total
print(menor)