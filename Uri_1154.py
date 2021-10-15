total = 0
count = 1
while True:
    idade = float(input())
    if idade < 0 :
        print(f'{media:.2f}')
        break
    total +=idade
    media = total/count
    count += 1  