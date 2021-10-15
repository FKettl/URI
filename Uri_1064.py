total = 0
count = 0

for x in range(6):
    n = float(input())
    if n > 0:
        count += 1
        total += n

media = total / count

print(f'{count} valores positivos') 
print(f'{media:.1f}')    